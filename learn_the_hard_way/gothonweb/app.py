from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     greeting = 'Hello woooooorld'
#     # return f'Hello, {greeting}!'
#     # return render_template("index.html")  # else part in the template
#     return render_template("index.html", greeting=greeting)

@app.route("/hello", methods=['POST', 'GET'])
def index():
    greeting = 'Hello peppa pig.'
    # greet = request.args.get('greet', 'Helloooo')
    # name = request.args.get('name', 'Nobody')

    # if name:
    #     greeting = f"{greet}, {name}"
    # else:
    #     greeting = "Hello world."
    #
    # return render_template("index.html", greeting=greeting)

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")

if __name__ == "__main__":
    app.run()
