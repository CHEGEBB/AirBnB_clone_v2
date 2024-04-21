# Project: AirBnB Clone v2

## Description

This project implements various functionalities for a Flask web application based on an AirBnB clone. It involves creating routes to handle different functionalities such as displaying messages, handling dynamic URL routes, working with templates, interacting with a database, and more.

## Installation

1. Clone the GitHub repository [AirBnB_clone_v2](https://github.com/waltertaya/AirBnB_clone_v2).
2. Navigate to the `web_flask` directory.
3. Make sure you have Python 3 installed on your system.
4. Install Flask if not already installed: `pip install Flask`.

## Usage

1. Start the Flask web application using the provided scripts.
2. Access the specified routes in a web browser or using curl commands to interact with the application.
3. Explore different functionalities implemented in each route.

## Routes and Functionalities

### 0. Hello Flask!

- Displays "Hello HBNB!" when accessing the root route.

### 1. HBNB

- Displays "Hello HBNB!" when accessing the root route.
- Displays "HBNB" when accessing the "/hbnb" route.

### 2. C is fun!

- Displays "Hello HBNB!" when accessing the root route.
- Displays "HBNB" when accessing the "/hbnb" route.
- Displays "C &lt;text&gt;" when accessing the "/c/&lt;text&gt;" route.

### 3. Python is cool!

- Displays "Hello HBNB!" when accessing the root route.
- Displays "HBNB" when accessing the "/hbnb" route.
- Displays "C &lt;text&gt;" when accessing the "/c/&lt;text&gt;" route.
- Displays "Python &lt;text&gt;" when accessing the "/python/&lt;text&gt;" route.

### 4. Is it a number?

- Displays "Hello HBNB!" when accessing the root route.
- Displays "HBNB" when accessing the "/hbnb" route.
- Displays "C &lt;text&gt;" when accessing the "/c/&lt;text&gt;" route.
- Displays "Python &lt;text&gt;" when accessing the "/python/&lt;text&gt;" route.
- Displays "&lt;n&gt; is a number" when accessing the "/number/&lt;n&gt;" route if &lt;n&gt; is an integer.

### 5. Number template

- Displays "Hello HBNB!" when accessing the root route.
- Displays "HBNB" when accessing the "/hbnb" route.
- Displays "C &lt;text&gt;" when accessing the "/c/&lt;text&gt;" route.
- Displays "Python &lt;text&gt;" when accessing the "/python/&lt;text&gt;" route.
- Displays "&lt;n&gt; is a number" when accessing the "/number/&lt;n&gt;" route if &lt;n&gt; is an integer.
- Displays an HTML page showing "Number: &lt;n&gt;" when accessing the "/number_template/&lt;n&gt;" route if &lt;n&gt; is an integer.

### 6. Odd or even?

- Displays "Hello HBNB!" when accessing the root route.
- Displays "HBNB" when accessing the "/hbnb" route.
- Displays "C &lt;text&gt;" when accessing the "/c/&lt;text&gt;" route.
- Displays "Python &lt;text&gt;" when accessing the "/python/&lt;text&gt;" route.
- Displays "&lt;n&gt; is a number" when accessing the "/number/&lt;n&gt;" route if &lt;n&gt; is an integer.
- Displays an HTML page showing "Number: &lt;n&gt; is even|odd" when accessing the "/number_odd_or_even/&lt;n&gt;" route if &lt;n&gt; is an integer.

### 7. Improve engines

- Updates FileStorage and DBStorage classes to include a `close` method for proper handling of session closure and reloading data.
- Includes a demonstration of these changes.

### 8. List of states

- Displays an HTML page showing a list of all states sorted by name.
- Uses data fetched from the storage engine.

### 9. Cities by states

- Displays an HTML page showing a list of all states and their respective cities sorted by name.
- Uses data fetched from the storage engine.

13. Project Description:

This README file provides instructions for three Flask web applications developed as part of the AirBnB clone project (version 2). Each application serves a different purpose and utilizes the Flask framework along with SQLAlchemy for database management.

### 10. States and State

#### Mandatory Requirements:

- **Flask Web Application Setup:**
  - The application must listen on `0.0.0.0` on port `5000`.
  - Storage for fetching data from the storage engine (FileStorage or DBStorage) is required. This can be achieved using `from models import storage` and `storage.all(...)`.
  - To load all cities of a State:
    - If using DBStorage, utilize the `cities` relationship.
    - Otherwise, use the public getter method `cities`.
  - After each request, the current SQLAlchemy Session must be removed. This can be done by declaring a method to handle `@app.teardown_appcontext` and calling `storage.close()` within this method.

#### Routes:

- **/states:**
  - Displays an HTML page with a list of all State objects present in DBStorage, sorted by name (A->Z).
  - The page structure includes an H1 tag with the text "States" and a UL tag containing the list of State objects.
  - Each State is represented by a LI tag with the format `<state.id>: <B><state.name></B>`.

- **/states/<id>:**
  - Displays an HTML page with information about a specific State identified by its ID.
  - If a State object is found with the provided ID:
    - The page includes an H1 tag with the text "State: " and the name of the state.
    - It also includes an H3 tag with the text "Cities:" and a UL tag containing the list of City objects linked to the State, sorted by name (A->Z).
    - Each City is represented by a LI tag with the format `<city.id>: <B><city.name></B>`.
  - If no State object is found with the provided ID, the page displays an H1 tag with the text "Not found!".

#### Importing Data:

- Import the provided `7-dump.sql` file to have some data for testing.

#### Important Notes:

- Ensure that a running and valid `setup_mysql_dev.sql` exists in the AirBnB_clone_v2 repository.
- Make sure all tables are created when running `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`.

### 11. HBNB filters

#### Mandatory Requirements:

- **Flask Web Application Setup:**
  - The application must listen on `0.0.0.0` on port `5000`.
  - Storage for fetching data from the storage engine (FileStorage or DBStorage) is required. This can be achieved using `from models import storage` and `storage.all(...)`.
  - To load all cities of a State:
    - If using DBStorage, utilize the `cities` relationship.
    - Otherwise, use the public getter method `cities`.
  - After each request, the current SQLAlchemy Session must be removed. This can be done by declaring a method to handle `@app.teardown_appcontext` and calling `storage.close()` within this method.

#### Routes:

- **/hbnb_filters:**
  - Displays an HTML page similar to `6-index.html` from a previous project.
  - Copies specific CSS files (`3-footer.css`, `3-header.css`, `4-common.css`, and `6-filters.css`) from `web_static/styles/` to `web_flask/static/styles`.
  - Copies specific image files (`icon.png` and `logo.png`) from `web_static/images/` to `web_flask/static/images`.
  - Updates the `.popover` class in `6-filters.css` to enable scrolling and set a maximum height of 300 pixels.
  - Loads State, City, and Amenity objects from DBStorage and sorts them by name (A->Z).
  - Uses the content of `6-index.html` as the source code for the template `10-hbnb_filters.html`, replacing the content of the H4 tag under each filter title (H3 States and H3 Amenities) with `&nbsp;`.

#### Importing Data:

- Import the provided `10-dump.sql` file to have some data for testing.

#### Important Notes:

- Ensure that a running and valid `setup_mysql_dev.sql` exists in the AirBnB_clone_v2 repository.
- Make sure all tables are created when running `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`.

### 12. HBNB is alive!

#### Advanced Requirements:

- **Flask Web Application Setup:**
  - The application must listen on `0.0.0.0` on port `5000`.
  - Storage for fetching data from the storage engine (FileStorage or DBStorage) is required. This can be achieved using `from models import storage` and `storage.all(...)`.
  - To load all cities of a State:
    - If using DBStorage, utilize the `cities` relationship.
    - Otherwise, use the public getter method `cities`.
  - After each request, the current SQLAlchemy Session must be removed. This can be done by declaring a method to handle `@app.teardown_appcontext` and calling `storage.close()` within this method.

#### Routes:

- **/hbnb:**
  - Displays an HTML page similar to `8-index.html` from a previous project.
  - Copies specific CSS files (`3-footer.css`, `3-header.css`, `4-common.css`, `6-filters.css`, and `8-places.css`) from `web_static/styles/` to `web_flask/static/styles`.
  - Copies all files from `web_static/images/` to `web_flask/static/images`.
  - Updates the `.popover` class in `6-filters.css` to enable scrolling and set a maximum height of 300 pixels.
  - Updates `8-places.css` to ensure the price by night is always displayed on the top right of each place element, and the name is correctly aligned and visible.
  - Uses the content of `8-index.html` as the source code for the template `100-hbnb.html`, replacing the content of the H4 tag under each filter title (H3 States and H3 Amenities) with `&nbsp;`.
  - Ensures all HTML tags from objects are correctly used (e.g., `<BR />` generates a new line).
  - Loads State, City, Amenity, and Place objects from DBStorage and sorts them by name (A->Z).

#### Importing Data:

- Import the provided `100-dump.sql` file to have some data for testing.

#### Important Notes:

- Ensure that a running and valid `setup_mysql_dev.sql` exists in the AirBnB_clone_v2 repository.
- Make sure all tables are created when running `echo "quit" | HBN

## Repository

- GitHub Repository: [AirBnB_clone_v2](https://github.com/waltertaya/AirBnB_clone_v2)
