# FastAPI project
This project has been created to apply FastAPI to a ML project and it's part of a challenge called [Project-of-the-week](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-12-07-fastapi.md) that is being held by Datatalks.club.
# Content
## Enviroment
### I'll use a conda enviroment for this project
```sh
conda create -n fastapi python=3.9
conda activate fastapi
```
### Install fastapi
```sh
pip install fastapi
```
### Install other libraries that we'll use
```sh
pip install -r requirements.txt
```
### I'll use a previous model for this project. It has made on a previous project-of-the-week.
[churn-prediction-app](https://github.com/eeeds/churn-prediction-app)
# Tools
-   Python
-   Anaconda
-   Pandas
-   Scikit-Learn
-   FastAPI

# Learning FASTAPI
[Youtube Video](https://www.youtube.com/watch?v=0RS9W8MtZe4)
## First app
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
## Run the app
```sh
uvicorn main:app --reload
```

The command uvicorn main:app refers to:

-   main: the file main.py (the Python "module").
-   app: the object created inside of main.py with the line app = FastAPI().
-   --reload: make the server restart after code changes. Only use for development.