from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
  items = ["Python", "Java", "Kotlin", "Go"]
  return render_template('test.html', items=items)

app.run()