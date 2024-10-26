# This is for backend service
A template to create all public facing sites

# Local setup
1. Install [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#install-additional-python-versions)
2. Install the configured python version (3.12.7) using pyenv by running the command
    ```
    pyenv install
    ```
3. Create virtual environment by running the command
    ```
    pyenv virtualenv 3.12.7 venv
    ```
4. Activate the virtual environment by running the command
    ```
    pyenv activate venv
    ```
5. Install the project dependencies by running the command
    ```
    pip install -r requirements.txt
    ```
6. Start the development server by running the command
    ```
    python manage.py runserver
    ```
7. Go to http://127.0.0.1:8000/health/ API to make sure the server it up