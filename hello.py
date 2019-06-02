from flask import Flask 
from flask import request
from flask import url_for
import os
from flask import render_template

app = Flask(__name__)
# @app.route('/hello/')
# def hello_world():
#     return "hello world"

@app.route('/')
def index():
    return "index"

@app.route("/user/<path:username>")
def show_user_profile(username):
    return "user %s"%(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return 'post_id%d'%(post_id)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html',name=name)

# @app.route('/login/',methods = ['GET','POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()











if __name__ == '__main__' :
    app.run(host='0.0.0.0',debug=True)
