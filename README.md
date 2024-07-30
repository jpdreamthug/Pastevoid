# VoidPaste

VoidPaste is a Django-based web application for sharing text snippets, similar to Pastebin. The project includes features such as user authentication, paste categorization, and commenting.

Check this out https://void-paste.onrender.com/

## Test User
   ```sh
   login: test_admin
   password: 47B#vU3eEJ`B
   ```


## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Initial Data](#initial-data)


## Features

- User authentication (sign up, login, logout)
- Create, view, and delete pastes
- Categorize pastes
- Comment on pastes
- Pagination for pastes
- Detailed view for each paste

## Requirements

- Python 3.x
- Django 5.x
- Bootstrap 5 (for frontend styling)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/jpdreamthug/voidpaste.git
    cd voidpaste
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source env/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Initial Data

   To upload initial data in DB use this command:

   ```sh
   python manage.py loaddata initial_data.json
   ```

## Environment Variables

To keep sensitive information secure, you should use environment variables for configuration settings. You can use a `.env` file and the `python-decouple` package to manage these variables.


1. Create a `.env` file in the root directory of your project:
    ```sh
    touch .env
    ```

2. Add your environment-specific variables to the `.env` file. For example:
    ```ini
    DJANGO_SECRET_KEY=your_secret_key
    DJANGO_DEBUG=True
    ```

## Usage

1. Access the application at `http://127.0.0.1:8000/`.
2. Log in with your superuser credentials.
3. Create, view, and manage pastes.
