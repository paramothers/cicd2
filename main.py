from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to Python Flask World V2.0 from CI/CD pipeline - Paramasivam'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
