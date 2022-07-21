from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

#
# @bp.route('/hello')
# def hello_pybo():
#     return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    # question은 question_views.py에서 등록된 블루프린트의 별칭