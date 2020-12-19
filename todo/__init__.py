from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []

@app.route("/")
def index():
    return render_template("tasks.html", todos = todos)

@app.route("/addTask", methods = ["GET", "POST"])
def addTask():
    if request.method == "GET":
        return render_template("addTasks.html")
    else:
        todo = request.form.get("task")
        todos.append(todo)
        return redirect("/")