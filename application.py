import os
from dotenv import load_dotenv
from flask import Flask, redirect


load_dotenv()

SERVER_PORT = os.environ.get('SERVER_PORT')
REDIRECT_URL = os.environ.get('REDIRECT_URL')

application = Flask(__name__)


@application.route("/")
def hello():
    return redirect(REDIRECT_URL, code=301)


if __name__ == "__main__":
    application.run(port=SERVER_PORT)
