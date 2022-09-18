import os
import string
from distutils.log import debug
from flask import Flask, render_template, request
from werkzeug import *
from werkzeug.utils import secure_filename

app = Flask(__name__)

fileName = ""


@app.route("/")
def greeting():
    return render_template('index2.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        os.chdir('static')
        f.save(secure_filename(f.filename))
        os.chdir('../')
        fileName = f.filename
        # print(f.filename)
        # return f.filename
        return render_template('runEngine.html')


@app.route("/runOCR", methods=['GET', 'POST'])
def engine():
    # import module
    # from ast import main
    if request.method == 'POST':
        # import module
        from ast import main
        # import module
        # from ast import main
        from pdf2image import convert_from_path
        from PIL import Image
        import pytesseract
        import os
        import shutil
        def ocrfunc():
            # Store Pdf with convert_from_path function
            if (os.path.isdir('tempdata')):
                shutil.rmtree('tempdata')
            absolute_path = os.path.abspath('static')
            os.mkdir('tempdata')
            os.chdir('tempdata')

            images = convert_from_path('/home/lucky/PycharmProjects/pythonProject1/example.pdf')

            for i in range(len(images)):
                # Save pages as images in the pdf
                images[i].save('page' + str(i) + '.jpg', 'JPEG')

            os.chdir('../')
            file = open('myfile.txt', 'w')
            for i in range(len(images)):
                image = 'tempdata/page{}.jpg'.format(i)
                text = pytesseract.image_to_string(Image.open(image), lang="eng")
                file.write(text)
            file.close()
            shutil.rmtree('tempdata')

        ocrfunc()
        return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
