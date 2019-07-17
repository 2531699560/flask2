from flask import Blueprint, render_template


app3_blueprint = Blueprint('app03', __name__)

@app3_blueprint.route('/index')
def index():
    return render_template("copy.html")

