from flaks import requests, render_template
from flask import Blueprint as Blueprint

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html",
                           name=requests.args['name']]
    )