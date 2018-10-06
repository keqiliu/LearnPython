from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     greeting = 'Hello woooooorld'
#     # return f'Hello, {greeting}!'
#     # return render_template("index.html")  # else part in the template
#     return render_template("index.html", greeting=greeting)

# @app.route("/hello", methods=['POST', 'GET'])
# def index():
#     greeting = 'Hello peppa pig.'
#     # greet = request.args.get('greet', 'Helloooo')
#     # name = request.args.get('name', 'Nobody')
#
#     # if name:
#     #     greeting = f"{greet}, {name}"
#     # else:
#     #     greeting = "Hello world."
#     #
#     # return render_template("index.html", greeting=greeting)
#
#     if request.method == "POST":
#         name = request.form['name']
#         greet = request.form['greet']
#         greeting = f"{greet}, {name}"
#         return render_template("index.html", greeting=greeting)
#     else:
#        return render_template("hello_form.html")

@app.route("/")
def index():
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))

@app.route("/game", methods = ['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name and room_name != 'generic_death':
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game"))

app.secret_key = 'aiyoyoyoyo'

if __name__ == "__main__":
    app.run()
