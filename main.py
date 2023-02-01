from flask import Flask, render_template
import utils
import templates


app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utils.get_all()
    return render_template("list.html", candidates=candidates)

@app.route('/candidate/<int:pk>')
def img_candidate(pk):
    candidate = utils.get_by_pk(pk)
    return render_template('card.html', candidate=candidate)


@app.route("/candidate/<skills>")
def get_candidates_skills(skills):
    return ""

if __name__ == '__main__':
    app.run(debug=True)