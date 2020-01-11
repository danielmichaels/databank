from flask import render_template

from web.core import core


@core.route('/')
def index():
    return render_template('index.html', title="Flask App")
