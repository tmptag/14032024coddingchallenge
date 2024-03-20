from invoke import task
import os
import time


@task
def install_requirements(c):
    """
    for installing the requirements use this command from the terminal.
    inv install-requirements
    """
    try:
        dependencies_start_time = time.time()
        c.run("pip install -r requirements.txt")
        print("=====REQUIREMENTS INSTALLED SUCCESSFULLY=======")

    except:
        print("failure in setup")


# no-longer needed, as we are directly calling it from the any file ASAP.
# we can use it latter in case we want to debug the alchemy model, if error occurs.
@task
def model_setup(c):
    try:
        # comment 1 for testing, for proper working comment 2
        # c.run("python3 Dataset/modelcreation.py")
        c.run("python3 Dataset/_modelcreation.py")
        print("model set up successfully.")

    except:
        print("failure in sqlalchamy model initializer")


@task
def dataset_loader(c):
    try:
        """
        this function will be used in the dataset insertion to the database, using sqlalchamy model validation.
        inv dataset-loader
        """
        # comment 1 for testing, for proper working comment 2
        # c.run("python3 Dataset/modelcreation.py")
        # c.run("python3 Dataset/datasetloader.py")
        c.run("python3 Dataset/_datasetloader.py")
        print("=====DATABASE LOADED.=======")
    except:
        print("failure in dataset loader")


@task
def runserver(c):
    try:
        """
        for running the fastapi app on the server.
        inv runserver
        """
        c.run("python3 main.py")
    except:
        print("failure in staring server.")
