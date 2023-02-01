from flask import Flask

from application.hw_6_app.csv_reader import csv_reader
from application.hw_6_app.read_text import read_text
from application.hw_6_app.generator_email import generator_email
from application.hw_6_app.astronaut_counter import austronaut_counter

app = Flask(__name__)


@app.route("/get-content/")
def task_1_text():  # put application's code here
    return read_text()


@app.route("/generate-users/")
def task_2_generator():  # put application's code here
    return generator_email()


@app.route("/space/")
def task_3_astronaut():  # put application's code here
    return austronaut_counter()


@app.route("/mean/")
def task_4_csv():
    # only read, no more...
    return csv_reader()


if __name__ == "__main__":
    app.run()
