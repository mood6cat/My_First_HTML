from flask import Flask, render_template
import utils


app = Flask(__name__)


@app.route('/')
def page_index():
    candidate = utils.get_all()
    return render_template("list.html", candidate=candidate)


@app.route('/candidate/<int:pk>')
def img_candidate(pk):
    candidate = utils.get_by_pk(pk)
    return render_template('card.html', candidate=candidate)


if __name__ == '__main__':
    app.run(debug=True)