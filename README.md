# random_data

#### 介绍
生成随机数据
1. 生成随机密码
2. 生成随机用户名(中)
3. 生成随机手机号
4. 生成随机电子邮箱
5. 生成唯一ID
6. 生成随机车牌号
7. 生成随机双色球、大乐透彩票号码
8. 生成省市区县街道地址(计划)
9. 生成随机身份证
10. 生成随机公司名称
11. 生成随机url
12. 生成随机IP地址
13. 生成随机MAC地址
14. 生成随机文件（txt，doc）
15. 生成随机颜色值
16. 生成随机电影名字
17. 生成诗词歌词
18. 生成冷笑话
#### 软件架构
开发语言：python  
web框架：flask

#### 安装教程

```
1.git clone https://github.com/y2k00001/rangdom_data.git
2.python main.py
```
#### 在线体验
演示地址：https://random.neo-ai.cn/id?num=10

#### 使用说明

1. web方式返回生成的随机数据
~~~
req:http://127.0.0.1:5000/random/passwd
response: 
{
    code: 0,
    msg: "成功",
    data: [
        "9EBFFSX5"
    ]
}
~~~
2. 系统软件界面形式生成随机数据(计划)
    计划使用Nuitka来安装打包成exe ,目前只能打包成exe ，Mac系统的还未找到可行的方法。

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


