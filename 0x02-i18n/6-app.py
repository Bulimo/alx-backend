#!/usr/bin/env python3
""" flask simple api """
from flask import Flask, render_template, g
from flask_babel import Babel, gettext, request

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ babel config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app.config.from_object(Config)


@app.route('/')
def hello():
    """ Hello world """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """ determine the best match with supported languages """
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ returns a user dictionary """
    try:
        return users.get(int(request.args.get("login_as")))
    except Exception:
        return None


@app.before_request
def before_request():
    """ execute before all other functions """
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
