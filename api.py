from flask import Blueprint, request

from response import api_return
from utils import password, telphone, gen_name, gen_email, gen_unique_id, gen_plate_no, gen_lucky,gen_id_num

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


@random.route('/random/plate_num',methods=['GET'])
def plate():
    num = 1 if not request.args.get("num") else int(request.args.get("num"))
    return api_return("OK",data=gen_plate_no(num))

@random.route('/random/lucky_num',methods=['GET'])
def lucky():
    num = 1 if not request.args.get("num") else int(request.args.get("num"))
    return api_return("OK",data=gen_lucky(num))

@random.route('/random/id_num',methods=['GET'])
def id_num():
    num = 1 if not request.args.get("num") else int(request.args.get("num"))
    return api_return("OK",data=gen_id_num(num))

@random.route('/id',methods=['GET'])
def  unique_id():
    num = 1 if not request.args.get("num") else int(request.args.get("num"))
    return api_return("OK",data=gen_unique_id(num))

