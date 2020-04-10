<b>Daily Harvest Exercise</b>
  - This simple Flask app will provide a search page from which the user can search for their favorite Daily Harvest products by ingredient. If products are found that include the selected ingredient, they will be displayed on the search screen, otherwise, you will see no products. Organic Bananas are the default value selected in the dropdown.
  
<b>Steps to run project:</b>
  * Ensure that you have Flask installed (https://flask.palletsprojects.com/en/1.1.x/installation/)
  * Clone this repository
  * Navigate to the project root and run the Flask developement server using the following commands:
    * export FLASK_APP=daily_harvest.py (NOTE: you can run the server in debug mode by using: export FLASK_APP=development)
    * flask run
  * Once your server is running, you can navigate to http://127.0.0.1:5000/products/ and use the dropdown to find your new favorite snack!
