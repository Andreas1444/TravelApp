# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request, render_template
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
import pytesseract as tess
import googletrans
from googletrans import Translator
#pip install googletrans==4.0.0-rc1 to make it work
from PIL import Image
from main import *
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired    


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")



@app.route('/', methods=['GET',"POST"])
# ‘/’ URL is bound with hello_world() function.
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        text_from_image = translateIntoEnglish(getTextfromImage(file_path))
        popup_script = '''
                   <script>
                       alert("Image loaded successfully");
                   </script>
               '''

        return redirect(url_for('menu',filename=filename ,text_from_image=text_from_image))
    return render_template('index.html', form=form)

# @app.route('/menu/<filename>/<text_from_image>')
# def menu(filename, text_from_image):
#     return render_template('menu.html', filename=filename,text_from_image=text_from_image)

@app.route('/menu')
def menu():
    filename = request.args.get('filename')
    text_from_image = request.args.get('text_from_image')
   # text_from_image = text_from_image.pop(0)
    i=0
    while text_from_image[i]!='\n':
        i = i + 1
    text_from_image_without_title = text_from_image[i+1:]
    print(text_from_image)
    return render_template('menu.html', filename=filename, text_from_image=text_from_image_without_title)

@app.route('/success/<name>')
def success(name):
    name = getRecipe(name)
    return 'welcome %s' % name

@app.route('/recipe')
def recipe():
    # Decode the URL-encoded parameter if needed
    name = request.args.get('name')
    i = 0
    while name[i] != '-':
        i = i + 1
    # to remove the the price, so for example"- 10"
    name = name[:i]
    recipe = getRecipe(name)
    picture_url = getPicture(name)
    print(picture_url)
   # return '%s' % recipe
    return render_template('recipe.html', name_recipe = name, recipe = recipe, picture_url = picture_url)



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        #user contains now the name of the recipe
        user = translateIntoEnglish(user)

        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.

    app.run(debug=True)