from flask import render_template
from flask.ext.classy import FlaskView


class MetaView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('meta/index.html')
