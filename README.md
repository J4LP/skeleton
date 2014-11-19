J4Skeleton
==========

Basic application skeleton for J4LP applications. Ready to accept login from J4OAUTH.

You should change all mentions of skeleton (even in folder/filenames) to the name of your application.

	virtualenv .
	source bin/activate
	pip install -r requirements.txt
	python manage.py db upgrade
	python run.py

## What's in there

* [Flask](http://flask.pocoo.org/), a simple web framework in Python
* [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/), a SQL ORM
* [Flask-Assets](http://flask-assets.readthedocs.org/en/latest/), an assets manager (compile coffee and less files and much more)
* [Flask-Classy](https://pythonhosted.org/Flask-Classy/), a class based view that speeds up development
* [Flask-Login](https://flask-login.readthedocs.org/en/latest/), user session management
* [Flask-Migrate](http://flask-migrate.readthedocs.org/en/latest/) enables database migrations
* [Flask-Oauthlib](flask-oauthlib.readthedocs.org/en/latest/) adds OAuth support
* [Flask-Script](http://flask-script.readthedocs.org/en/latest/) adds CLI commands
* [Flask-WTF](flask-wtf.readthedocs.org/en/latest/) adds forms

## Add a blueprint and a view

A blueprint is a collection of views. Create a new file in the blueprints folder, say, `fancy.py`, here's the boilerplate:

```python
from flask import render_template
from flask.ext.classy import FlaskView


class FancyView(FlaskView):

    def index(self):
        return render_template('fancy/index.html')
```

Don't forget to modify the blueprints/\_\_init\_\_.py file to add `from .fancy import FancyView`.
            
Then create the folder `fancy` in `templates` and a new file called `index.html`:

```html+jinja
{% extends "_layouts/base.html" %}

{% block title %}Fancy View | {{ config.EVE.auth_name }}{% endblock %}

{% block body %}
    This is your skeleton application
{% endblock %}
```
And register the blueprint in the `app.py` file around the line 15:

```python
from skeleton.blueprints import AccountView, MetaView, FancyView
AccountView.register(app)
MetaView.register(app)
FancyView.register(app)
```

You should now be able to run the application and access that new view at `/fancy/`.

### Licence

The MIT License (MIT)

Copyright (c) [2014] [@adrien-f]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

