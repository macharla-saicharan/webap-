from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_name():
    return "Hello %s!"

app.run()



