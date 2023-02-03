from flask import Flask, render_template
import utils


app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utils.get_all()
    return render_template("list.html", candidates=candidates)


@app.route('/candidates/<int:pk>')
def img_candidate(pk):
    candidate = utils.get_by_pk(pk)
    return render_template('card.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def name_candidate(candidate_name):
    candidates = utils.get_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, cnt_candidates=len(candidates))

@app.route('/skill/<skill>')
def in_main_get_by_skill(skill):
    candidates = utils.get_by_skill(skill)
    return render_template('skill.html', candidates=candidates, cnt_candidates=len(candidates))

if __name__ == '__main__':
    app.run(debug=True)