# This is for backend service
A template to create all public facing sites

## To run the app in docker
1. Install [docker](https://docs.docker.com/get-docker/) and [docker compose](https://docs.docker.com/compose/install/)
2. Start Django application and MongoDB using docker
    ```
    docker-compose up -d
    ```
3. Go to http://127.0.0.1:8000/health/ API to make sure the server it up. You should see this response
    ```
    {
    "status": "UP"
    }
    ```
4. On making changes to code and saving, live reload will work in this case as well

## Local setup
1. Install [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
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
    python -m pip install -r requirements.txt
    ```
6. Create a `.env` file in the root directory, and copy the content from the `.env.example` file to it
7. Install [docker](https://docs.docker.com/get-docker/) and [docker compose](https://docs.docker.com/compose/install/)
8. Start MongoDB using docker
    ```
    docker-compose up -d db
    ```
9. Start the development server by running the command
    ```
    python manage.py runserver
    ```
10. Go to http://127.0.0.1:8000/health/ API to make sure the server it up. You should see this response
    ```
    {
    "status": "UP"
    }
    ```