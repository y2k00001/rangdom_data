'''
常用工具类
'''
import csv
import random
import string

from faker import Faker

from idworker import IdWorker


def get_random_num(length=8):
    '''
    # 获取指定长度随机数
    :param length:
    :return:
    '''
    random_num = ''
    for i in range(length):
        random_num = random_num + str(random.randint(0, 9))
    return random_num

def password(length=8, num=1):
    '''
    生成密码
    :param length: 密码长度
    :param num: 密码数量
    :return: 密码列表
    '''
    password_list = []
    for x in range(num):
        pw = str()
        characters = "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "1234567890" + "!@#$%^&*-_"
        for i in range(length):
            pw = pw + random.choice(characters)
        password_list.append(pw)
    return password_list

def get_tle_phone(phone_list=[]):
    '''
    # 随机生成一个手机号码
    :param phone_list:
    :return:
    '''
    second = random.choice([3, 4, 5, 7, 8])  # 第二位值，从此列表随机生成
    third = {
        3: random.randint(0, 9),
        4: random.choice([5, 7]),
        5: random.choice([0, 1, 2, 3, 5, 6, 7, 8, 9]),
        7: random.choice([6, 7, 8]),
        8: random.randint(0, 9)
    }[second]  # 根据second的值，来生成第3位的值
    phone_number = str(1) + str(second) + str(third) + get_random_num(8)  # 四组字符相加，生成手机号
    counts = phone_list.count(phone_number)
    if counts:
        return get_tle_phone(phone_list)
    return phone_number

def telphone(num=1):
    '''
    生成电话号码
    :param num: 电话号码数量
    :return: 电话号码列表
    '''
    phone_list=[]
    for x in range(num):
        phone_list.append(get_tle_phone(phone_list))
    return phone_list

def gen_email(num=1, len=8, list_email=None):
    '''
    生成电子邮箱
    :param num: 电子邮箱数量
    :param len: 电子邮箱长度
    :param list_email: 电子邮箱域名
    :return: 电子邮箱列表
    '''
    #根据指定范围，随机邮箱字符串最大最小长度
    if list_email is None:
        list_email = ['@163.com', '@sina.com', '@qq.com', '@126.com']
    #可供选的字符串
    str = ""
    letters1 = string.ascii_letters  #字母
    letters2 = string.digits  # 数字

    email_list=[]
    for x in range(num):
        # 随机邮箱后缀,从一个存储邮箱的list里选择
        email_form = random.choice(list_email)
        for i in range(1,3):
            str = str+letters1+letters2+letters2+letters2+letters2
        #通过join()方法连接字符,去掉空格
        email_str = ''.join(random.sample(str,len))
        # 字符串连接,加上邮箱后缀
        email_list.append(email_str+email_form)

    return email_list

def gen_unique_id(num=1):
    """
    根据雪花算法生成分布式唯一ID，欢迎来搞测试
    :param num:
    :return:
    """
    ids =[]
    worker = IdWorker(1,2,0)
    for x in range(num):
        id = str(worker.get_id())
        ids.append(id)
    return ids

def gen_plate_no(num):
    '''
    生成随机车牌号
    :param num:数量
    :return:车牌号列表
    '''
    plat_numbers = []
    char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
    char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # 车牌号中没有I和O，可自行百度
    char2 = '1234567890'
    len0 = len(char0) - 1
    len1 = len(char1) - 1
    len2 = len(char2) - 1
    for x in range(num):
        code = ''
        index0 = random.randint(1, len0)
        index1 = random.randint(1, len1)
        code += char0[index0]
        code += char1[index1]
        for i in range(1, 6):
            index2 = random.randint(1, len2)
            code += char2[index2]
        plat_numbers.append(code)
    return plat_numbers

def gen_id_num(num):
    '''
    生成中国身份证
    :param num:
    :return:
    '''
    id_nums = []
    fake = Faker("zh_CN")
    for x in range(num):
        id_nums.append(fake.ssn())
    return id_nums

def gen_com(num):
    '''
    生成公司名称
    :param num:
    :return:
    '''
    com_list = []
    fake = Faker("zh_CN")
    for x in range(num):
        com_list.append(fake.company())
    return com_list

def gen_url(num):
    '''
    生成url网址
    :param num:
    :return:
    '''
    url_list = []
    fake = Faker("zh_CN")
    for x in range(num):
        url_list.append(fake.url())
    return url_list


def gen_lucky(num):
    '''
    生成大乐透、双色球随机号码
    :param num:
    :return:
    '''
    lucky_numbers = {'daletou':[],'shuangseqiu':[]}
    for x in range(num):
        daletou = get_resultStr(33, 6)+' '+ get_resultStr(16, 1)
        shuangseqiu = get_resultStr(35, 5)+' '+ get_resultStr(12, 2)
        lucky_numbers['daletou'].append(daletou)
        lucky_numbers['shuangseqiu'].append(shuangseqiu)
    return lucky_numbers
def get_resultStr(totalCount, resultCount):
  elements = [x + 1 for x in range(totalCount)]
  retStr = ''
  for i in range(resultCount):
    res = elements[random.randint(0,len(elements)-1)]
    elements.remove(res)
    retStr += ' ' + str(res)
  return retStr


def gen_name(num):
    '''
    生成中文姓名
    :param num: 姓名数量
    :return: 姓名列表
    '''
    name_list = []
    for x in range(num):
        name = popular()
        name_list.append(name)
    return name_list
def last_name():
    family_name_list= [
      "赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤",
      "许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水",
      "窦","章","云","苏","潘","葛","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞",
      "任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤","滕","殷","罗","毕",
      "郝","邬","安","常","乐","于","时","傅","皮","卞","齐","康","伍","余","元","卜","顾","孟","平",
      "黄","和","穆","萧","尹","姚","邵","湛","汪","祁","毛","禹","狄","米","贝","明","臧","计","伏",
      "成","戴","谈","宋","茅","庞","熊","纪","舒","屈","项","祝","董","梁","杜","阮","蓝","闵","席",
      "季","麻","强","贾","路","娄","危","江","童","颜","郭","梅","盛","林","刁","钟","徐","邱","骆",
      "高","夏","蔡","田","樊","胡","凌","霍","虞","万","支","柯","昝","管","卢","莫","经","房","裘",
      "缪","干","解","应","宗","丁","宣","贲","邓","郁","单","杭","洪","包","诸","左","石","崔","吉",
      "钮","龚","程","嵇","邢","滑","裴","陆","荣","翁","荀","羊","于","惠","甄","曲","家","封","芮",
      "羿","储","靳","汲","邴","糜","松","井","段","富","巫","乌","焦","巴","弓","牧","隗","山","谷",
      "车","侯","宓","蓬","全","郗","班","仰","秋","仲","伊","宫","宁","仇","栾","暴","甘","钭","厉",
      "戎","祖","武","符","刘","景","詹","束","龙","叶","幸","司","韶","郜","黎","蓟","溥","印","宿",
      "白","怀","蒲","邰","从","鄂","索","咸","籍","赖","卓","蔺","屠","蒙","池","乔","阴","郁","胥",
      "能","苍","双","闻","莘","党","翟","谭","贡","劳","逄","姬","申","扶","堵","冉","宰","郦","雍",
      "却","璩","桑","桂","濮","牛","寿","通","边","扈","燕","冀","浦","尚","农","温","别","庄","晏",
      "柴","瞿","阎","充","慕","连","茹","习","宦","艾","鱼","容","向","古","易","慎","戈","廖","庾",
      "终","暨","居","衡","步","都","耿","满","弘","匡","国","文","寇","广","禄","阙","东","欧","殳",
      "沃","利","蔚","越","夔","隆","师","巩","厍","聂","晁","勾","敖","融","冷","訾","辛","阚","那",
      "简","饶","空","曾","毋","沙","乜","养","鞠","须","丰","巢","关","蒯","相","查","后","荆","红",
      "游","郏","竺","权","逯","盖","益","桓","公","仉","督","岳","帅","缑","亢","况","郈","有","琴",
      "归","海","晋","楚","闫","法","汝","鄢","涂","钦","商","牟","佘","佴","伯","赏","墨","哈","谯",
      "篁","年","爱","阳","佟","言","福","南","火","铁","迟","漆","官","冼","真","展","繁","檀","祭",
      "密","敬","揭","舜","楼","疏","冒","浑","挚","胶","随","高","皋","原","种","练","弥","仓","眭",
      "蹇","覃","阿","门","恽","来","綦","召","仪","风","介","巨","木","京","狐","郇","虎","枚","抗",
      "达","杞","苌","折","麦","庆","过","竹","端","鲜","皇","亓","老","是","秘","畅","邝","还","宾",
      "闾","辜","纵","侴","万俟","司马","上官","欧阳","夏侯","诸葛","闻人","东方","赫连","皇甫","羊舌",
      "尉迟","公羊","澹台","公冶","宗正","濮阳","淳于","单于","太叔","申屠","公孙","仲孙","轩辕","令狐",
      "钟离","宇文","长孙","慕容","鲜于","闾丘","司徒","司空","兀官","司寇","南门","呼延","子车","颛孙",
      "端木","巫马","公西","漆雕","车正","壤驷","公良","拓跋","夹谷","宰父","谷梁","段干","百里","东郭",
      "微生","梁丘","左丘","东门","西门","南宫","第五","公仪","公乘","太史","仲长","叔孙","屈突","尔朱",
      "东乡","相里","胡母","司城","张廖","雍门","毋丘","贺兰","綦毋","屋庐","独孤","南郭","北宫","王孙"
    ]
    return random.choice(family_name_list)
def popular():
    single=['筱','若','湘','玥','媱','汐','瑄','羽','霏','影','沫','燕','泠','梓','言','斓','璃','落','矞','琅','湛','露','浅',
            '采','然','流','梦','溪','墨','染','冰','绡','舞','野','凝','纱','菡','弈','宸','烨','岚','漠','庭','城','途','伯',
            '弘','枭','律','哲','凌','沙','辞','汉','恺','斯','烟','暘','寒','离','尘','崖','伞','谪','泽','扬','赫','穆','独',
            '绝','轩''殇','墨','言','深','渊','溪','沐','钰','辰','浩','曦','璃','枫','苏','唐','瑶','君','麟','笙','陌','柯',
            '寒','瀚','泽','绝','尘','清','玖','轩','薛','洛','雨','煜','晗','念','展']
    double = ['以寒','寒香','小凡','代亦','梦露','映波','友蕊','寄凡','怜蕾','雁枫','水绿','曼荷','笑珊','寒珊','谷南','慕儿','夏岚','友儿',
              '小萱','紫青','妙菱','冬寒','曼柔','语蝶','青筠','夜安','觅海','问安','晓槐','雅山','访云','翠容','寒凡','晓绿','以菱','冬云',
              '含玉','访枫','含卉','夜白','冷安','灵竹','醉薇','元珊','幻波','盼夏','元瑶','迎曼','水云','访琴','谷波','乐之','笑白','之山',
              '妙海','紫霜','平夏','凌旋','孤丝','怜寒','向萍','凡松','青丝','翠安','如天','凌雪','绮菱','代云','南莲','寻南','春文','香薇',
              '冬灵','凌珍','采绿','天春','沛文','紫槐','幻柏','采文','春梅','雪旋','盼海','映梦','安雁','映容','凝阳','访风','天亦','平绿',
              '盼香','觅风','小霜','雪萍','半雪','山柳']
    name = last_name()
    if random.choice([True,False]) == True:
        name += random.choice(double)
    else:
        name+= random.choice(single)
    return (name)


