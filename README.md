# Weather API

This Flask application serves as an API for accessing weather data from various stations. It allows users to view temperature records for specific stations and dates, as well as retrieve all available data for a given station or yearly data.
Features

    Home Page: Displays a list of weather stations in a tabular format.
    API Endpoints:
        Get temperature for a specific station and date.
        Retrieve all data for a specific station.
        Fetch yearly data for a specific station.

Prerequisites

Before running the application, ensure you have the following installed:

    Python 3.x
    Flask
    Pandas

Installation

You can install the necessary Python libraries using pip:

bash

pip install Flask pandas

Files
1. app.py

This is the main application file containing the Flask app and all the API endpoints.
Routes:

    /: Home page that displays the list of weather stations.
    /api/v1/<station>/<date>: Returns the temperature for the specified station and date.
    /api/v1/<station>: Returns all data for the specified station.
    /api/v1/yearly/<station>/<year>: Returns yearly data for the specified station.

2. Data_small/

This directory contains the data files used by the application:

    stations.txt: Contains a list of weather stations.
    TG_STAIDxxxxxx.txt: Contains temperature records for specific stations, where xxxxxx is the station ID.

3. templates/Home.html

This file contains the HTML template for the home page where the list of weather stations is displayed.
Running the Application

    Clone the repository:

    bash

git clone https://github.com/your-repo/weather-data-api.git

Navigate to the project directory:

bash

cd weather-data-api

Run the Flask application:

bash

    python app.py

    Open your browser and go to http://localhost:5001/ to view the home page.

Example API Requests

    Get temperature for a specific station and date:

    bash

GET /api/v1/123456/2024-10-11

Retrieve all data for a specific station:

bash

GET /api/v1/123456

Fetch yearly data for a specific station:

bash

GET /api/v1/yearly/123456/2024
