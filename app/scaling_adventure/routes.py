import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def home():
  return render_template('index.html')

"""
Upload the given file to `UPLOAD_FOLDER`
"""
@app.route('/upload', methods= ['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return str(1)
    return str(0)

if __name__ == '__main__':
  app.run(debug=True)
