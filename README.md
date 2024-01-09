
# Travel App

This browser app is designed to help travelers around the world when visiting a restaurant in a different country. For this, the project showcases the use of machine learning and computer vision.

## Use case

The app has 2 functionalities. The Traveler can upload a recently taken picture of a menu that is in a foreign language. The menu gets translated into english and every menu item can be clicked to see a picture of the meal and its recipe. The second functionality is to calculate the amount of tips that is recommended to leave to the waiter. After inserting some neccesary data(total amount, amount of persons, etc.) the traveler gets an estimate of the tip amount

## What to install / Steps:







Run the following comand in the terminal

```bash
  pip install pytesseract
```
Download and install the tesseract.exe from:
 https://github.com/UB-Mannheim/tesseract/wiki

 Update if neccesary the 10 line of code from the main.py file:

```bash
10   tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
After that, to make the Flask app running write this lines in the termianl:
```bash
pip install virtualenv
virtualenv venv
```

To Activate the virtual environment, run the powershell as admin and Type the following command:
```bash
set-executionpolicy remotesigned
```
Now, you will be prompted to change the execution policy. Please type A. This means Yes to all.

After that use:
```bash
pip install Flask
```
Now everything should run smoothly.


## How to run the app

Just run the flaskTravel.py file and type http://127.0.0.1:5000 in your browser. Select an image from your PC or just use the Example.png file I provided in the repository. Click on upload file and you should see your uploaded image as well as the translation of the text found in your image.



