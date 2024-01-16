from flask import Flask, render_template, redirect, url_for
from forms import MoviesForm

app = Flask(__name__)
app.config['SECURITY_KEY']='08e9603c58c3362667f14983f4ee365b6efd930719d7c10a'

movies_list = [{'title': 'Ludo',
                'plot':'Four seemingly different stories intertwine in a game of fate and chance that includes a scandalous sex tape, a suitcase full of money and unsettled scores.',
                'released':'12-11-2020',
                'platform':'Netflix',
                'available':True}]

@app.route('/', methods=('GET', 'POST'))
def index():
    movie_form = MoviesForm()
    render_template('index.html', form=movie_form)