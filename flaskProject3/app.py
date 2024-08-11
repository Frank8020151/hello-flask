from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/hello',methods=['POST'])
def hello_world():  # put application's code here
    return f"hello,{request.form.get('name')}!"

@app.route('/')
def home():
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
