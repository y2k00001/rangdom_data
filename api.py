from flask import Blueprint, request

from response import api_return
from utils import password, telphone, gen_name, gen_email

random = Blueprint("random", __name__)


@random.route('/random/passwd',methods=['GET'])
def passwd():
    len = 8 if not request.args.get("len") else int(request.args.get("len"))
    num = 1 if not request.args.get("num") else int(request.args.get("num"))
    list = password(len,num)
    return  api_return("OK",data=list )


@random.route('/random/phone',methods=['GET'])
def phone():
    num = 1 if not request.args.get("num") else int(request.args.get("num"))
    return api_return("OK",data=telphone(num))


@random.route('/random/name',methods=['GET'])
def name():
    num = 1 if not request.args.get("num") else int(request.args.get("num"))
    return api_return("OK",data=gen_name(num))


@random.route('/random/email',methods=['GET'])
def email():
    len = 8 if not request.args.get("len") else int(request.args.get("len"))
    num = 1 if not request.args.get("num") else int(request.args.get("num"))
    return api_return("OK",data=gen_email(num,len))

