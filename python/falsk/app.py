from flask import Flask,render_template,request,g,session,url_for
import MySQLdb
import os
import json

#flask的实例
app = Flask(__name__,static_folder="../../p_img")

#MySQL配置
host = 'localhost'
user = 'root'
password = '123'
database = 'gaokao'

# 建立数据库连接
db = MySQLdb.connect(host=host, user=user, passwd=password, db=database)




#填空题
#获取图片信息
@app.route("/blank",methods = ['POST', 'GET'])
def blank():


    #获取没有改完的学生
    db = MySQLdb.connect(host=host, user=user, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT id FROM stu_test WHERE blank IS NULL")

    #查询结果 只查一个
    data = cursor.fetchone()

    #查询结果个数
    count = cursor.rowcount

    if count == 0:
        return "改完了！！"

    data = {
        "img_src": 'p_img/blank/' + data[0] + '.jpg',
        "id": data[0]

    }


    response = json.dumps(data)  # 将python的字典转换为json字符串
    return response,200,{"Content-Type":"application/json"}




@app.route("/sub_blank",methods=['POST','GET'])
def sub_blank():
        #登分
    id = request.values.get("id")
    point = request.values.get("point")

    db = MySQLdb.connect(host=host, user=user, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("update stu_test set blank = %s where id = %s",(point,id,))
    db.commit()

@app.route("/login",methods=['POST','GET'])
def login():
    id = request.values.get("id")
    pwd = request.values.get("pwd")

    db = MySQLdb.connect(host=host, user=user, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * from teacher where id = %s and pwd = %s",(id,pwd,))

    #查询结果 只查一个
    data = cursor.fetchone()

    #查询结果个数
    count = cursor.rowcount

    if count != 0:
        return "ok"
    else:
        return "no"
    
    


#main函数
if __name__ == '__main__':
    app.run(debug=True)
