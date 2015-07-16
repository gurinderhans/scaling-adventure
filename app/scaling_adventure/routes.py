import os, json
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
from recognizer.recognize import Recognizer

# load json data
json_config = json.load(open('config.json'))

UPLOAD_FOLDER = json_config['uploads_folder']
EIGEN_MODELS_FOLDER = json_config['eigen_models_folder']
DETECTED_IMAGES_FOLDER = json_config['detected_images_folder']
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['EIGEN_MODELS_FOLDER'] = EIGEN_MODELS_FOLDER
app.config['DETECTED_IMAGES_FOLDER'] = DETECTED_IMAGES_FOLDER

#
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def home():
  return render_template('index.html')

"""
- Upload the given file to `UPLOAD_FOLDER`
- Then compare image and send back to client
"""
@app.route('/upload', methods= ['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        fileSavePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(fileSavePath)

        recognizer_data = []
        # heavy processing here....
        recognizer = Recognizer(app.config['EIGEN_MODELS_FOLDER'], fileSavePath, 1000)
        for i in os.listdir(app.config['EIGEN_MODELS_FOLDER']):
            compared_data = recognizer.compareWith(os.path.join(app.config['EIGEN_MODELS_FOLDER'], i), os.path.join(app.config['DETECTED_IMAGES_FOLDER'], i.split(".")[0].split("_")[1]))
            recognizer_data.append(compared_data)

        return json.dumps(recognizer_data)

    return str(0)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
