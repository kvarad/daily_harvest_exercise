from flask import Flask, render_template, request

import os
import json


app = Flask(__name__)

@app.route('/products/', methods=['POST', 'GET'])
def search_products():
    """
    Main entry point from the search page. If a GET request is made, we return
    only the ingredients to search by. A POST request uses the ingredient ID to
    identify the products containing that ingredient.
    """
    # context is a dict which will contain all vars to render in the template
    context = {}

    ingredients = get_ingredients()
    context['ingredients'] = ingredients

    if request.method == "POST":
        ingredient_id = request.form['ingredient_id']
        ingredient_name = get_ingredient_name_by_id(ingredient_id, ingredients)
        products = find_foods_by_ingredient(ingredient_id)
        context['products'] = products
        context['ingredient_name'] = ingredient_name

    return render_template('search.html', context=context)


def get_ingredients():
    """
    Parses the ingredients.json file and provides a dictionary of ingredients
    """
    data = parse_json_file('ingredients.json')
    return data['ingredients']

def get_ingredient_name_by_id(ingredient_id, ingredients):
    """
    Accepts the ingredient ID and provides the corresponding ingredient name
    """
    ingredient_id = int(ingredient_id)
    for ingredient in ingredients:
        if ingredient['id'] == ingredient_id:
            return ingredient['name']

def find_foods_by_ingredient(ingredient_id):
    """
    Accepts an integer ingredient_id, finds the products which contain the item
    and returns a list of found found_products

    args:
    ingredient_id: (int)

    return:
    found_products: (list)
    """
    found_products = []
    data = parse_json_file('products.json')

    # iterate through the products and see if they contain the ingredient
    for val in data['products']:
        if int(ingredient_id) in val['ingredient_ids']:
            found_products.append(val['name'])

    return found_products

def parse_json_file(file_name):
    """
    Accepts a json filename to parse from the static dir and returns a json
    payload of parsed data.

    args:
    file_name: (string)

    return:
    data: (json)
    """
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', file_name)
    data = json.load(open(json_url))

    return data
