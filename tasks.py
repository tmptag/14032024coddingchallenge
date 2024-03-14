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
@task
def model_setup(c):
    try:
        c.run("python3 Dataset/modelcreation.py")
    except:
        print("failure in sqlalchamy model initializer")


@task
def dataset_loader(c):
    try:
        c.run("python3 Dataset/datasetloader.py ")
        print("=====DATABASE LOADED.=======")
    except:
        print("failure in dataset loader")


@task
def runserver(c):
    try:
        c.run("python3 main.py")
    except:
        print("failure in staring server.")
