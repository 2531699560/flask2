from flask import Blueprint, render_template


app2_blueprint = Blueprint('app02', __name__)

@app2_blueprint.route('/index')
def index():
    return render_template("copy.html")

