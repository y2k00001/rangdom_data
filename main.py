from flask import Flask,request

from api import random
from response import api_return
from utils import password, telphone, gen_email, gen_name

app = Flask(__name__)

app.register_blueprint(random)



if __name__ == '__main__':
    app.run(host='127.0.0.1')

