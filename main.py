import pytesseract as tess
import googletrans
from googletrans import Translator
from flask import Flask
#pip install googletrans==4.0.0-rc1 to make it work
from PIL import Image
import requests

translator = Translator()
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def getTextfromImage(image_path):
    img = Image.open(image_path)
    text = tess.image_to_string(img)
    return text
def translateIntoEnglish(word):
    return translator.translate(word, dest='en').text

def getPicture(recipe):
    api_key = '8f7185331a724f04962bad0fc3b1d196'
    base_url = 'https://api.spoonacular.com/'

    # Step 1: Search for recipes related to the given text
    search_endpoint = 'recipes/search'
    search_params = {
        'apiKey': api_key,
        'query': recipe,
        'number': 1,  # Retrieve only 1 result for simplicity, you can adjust this as needed
    }

    search_response = requests.get(f'{base_url}{search_endpoint}', params=search_params)

    if search_response.status_code == 200:
        # Extract the recipe ID from the search result
        search_result = search_response.json()
        if search_result['results']:
            recipe_id = search_result['results'][0]['id']

            # Step 2: Get information about the specific recipe by ID
            recipe_endpoint = f'recipes/{recipe_id}/information'
            recipe_params = {
                'apiKey': api_key,
            }

            recipe_response = requests.get(f'{base_url}{recipe_endpoint}', params=recipe_params)

            if recipe_response.status_code == 200:
                # Parse and return the URL of the recipe image
                recipe_data = recipe_response.json()
                image_url = recipe_data.get('image', '')
                return image_url

            else:
                return f"Error retrieving recipe information: {recipe_response.status_code} - {recipe_response.text}"

        else:
            return f"No recipes found for {recipe}."

    else:
        return f"Error searching for recipes: {search_response.status_code} - {search_response.text}"



def getRecipe(text):
    api_key = '8f7185331a724f04962bad0fc3b1d196'
    base_url = 'https://api.spoonacular.com/'


    # Step 1: Search for recipes related to 'Hamburger'
    search_endpoint = 'recipes/search'
    search_params = {
        'apiKey': api_key,
        'query': text,
        'number': 1,  # Retrieve only 1 result for simplicity, you can adjust this as needed
    }

    search_response = requests.get(f'{base_url}{search_endpoint}', params=search_params)

    if search_response.status_code == 200:
        # Extract the recipe ID from the search result
        search_result = search_response.json()
        if search_result['results']:
            recipe_id = search_result['results'][0]['id']

            # Step 2: Get information about the specific recipe by ID
            recipe_endpoint = f'recipes/{recipe_id}/information'
            recipe_params = {
                'apiKey': api_key,
            }

            recipe_response = requests.get(f'{base_url}{recipe_endpoint}', params=recipe_params)

            if recipe_response.status_code == 200:
                # Parse and print the ingredients
                recipe_data = recipe_response.json()
                ingredients = recipe_data.get('extendedIngredients', [])

                if ingredients:
                   ingredientsList = ""
                   for ingredient in ingredients:
                       ingredientsList = ingredientsList + f"- {ingredient['original']+'\n'}"

                   return ( ingredientsList)



                else:
                    return (f"No ingredients found for {text}.")

            else:
              return (f"Error retrieving recipe information: {recipe_response.status_code} - {recipe_response.text}")

        else:
           return (f"No recipes found for {text}.")

    else:
        return(f"Error searching for recipes: {search_response.status_code} - {search_response.text}")


#img = Image.open('dessert.png')
#text = tess.image_to_string(img)
#text = translateIntoEnglish(text)
#print(text)
#print(getRecipe(text))




# Replace 'YOUR_API_KEY' with your actual Spoonacular API key

