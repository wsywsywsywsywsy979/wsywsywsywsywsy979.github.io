from flask import Flask, render_template,request  #引入包中要使用的类

app = Flask(__name__, static_url_path='/resources', static_folder='./resources', template_folder='./../templates')

# 返回页面---------------------------------------------
@app.route('/SC', methods=['GET', 'POST']) # SC
def SC():
    return render_template("sc.html") 

@app.route('/LIB', methods=['GET', 'POST']) # LIB
def LIB():
    return render_template("lib.html") 

@app.route('/AS', methods=['GET', 'POST']) # AS
def AS():
    return render_template("as.html") 

@app.route('/UAS', methods=['GET', 'POST']) # AS
def UAS():
    return render_template("uas.html") 

@app.route('/', methods=['GET', 'POST']) # 主页面 
def index():
    return render_template("index.html") # 只显示结果
    # return render_template("test2.html") # 只显示结果
    # template_folder 设置的路径下的 index.html
#------------------------------------------------------

# 接收打分结果----------------------------------------
# @app.route('/SC__n', methods=['GET', 'POST']) # SC自然度打分
# def SC_n():
#     return "sc_n"
# @app.route('/SC__s', methods=['GET', 'POST']) # SC相似度打分
# def SC_n():
#     return "sc_n" # 
# 感觉可以直接在html文件中使用javascrip来计算即可

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3306) # 这样设置是对的，设置之后程序会自动给出对应的ip:10.134.124.16
    # app.run(debug=True)
