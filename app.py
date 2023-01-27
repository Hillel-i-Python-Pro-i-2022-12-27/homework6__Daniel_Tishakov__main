from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'\

@app.route('/daniel')
def hello():  # put application's code here
    return 'Hello Daniel!'

@app.route('/hi/<name>')
def hello_hi(name: str = "jack"):  # put application's code here
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run()
