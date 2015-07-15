import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
from recognizer.recognize import Recognizer

UPLOAD_FOLDER = '/Users/ghans/Documents/Tate-Hack/app/scaling_adventure/uploads/' # must be absolute
EIGEN_MODELS_FOLDER = '/' # must be absolute
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['EIGEN_MODELS_FOLDER'] = EIGEN_MODELS_FOLDER

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

        # TODO: processing here....
        # recognizer = Recognizer(app.config['EIGEN_MODELS_FOLDER'], fileSavePath, 1000)
        # recognizer.compareWith('eigenModel_1.xml')

        return str(1)
    return str(0)

if __name__ == '__main__':
  app.run(debug=True)
