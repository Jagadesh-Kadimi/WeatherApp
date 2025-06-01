# Django Weather App

## About

This is a Django-based web application that allows users to check the current weather for any city. It fetches weather data from the OpenWeatherMap API and displays a relevant background image using Google Custom Search.

## Features

- Search weather by city name
- Displays temperature, humidity, wind, sunrise/sunset, and more
- Shows a background image of popular places in the searched city

## Requirements

- Python 3.7+
- Django 3.2 or higher
- requests

## Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd Django_Weather_APP
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Open your browser and go to:**
   ```
   http://127.0.0.1:8000/
   ```

## Configuration

- The API keys for OpenWeatherMap and Google Custom Search are hardcoded in `views.py`. For production, move them to environment variables or Django settings for security.

## License

This project is for educational purposes.
