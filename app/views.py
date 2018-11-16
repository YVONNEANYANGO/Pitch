from flask import render_template
from app import app


def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to One-Minute-Pitch Website Online'
    return render_template('index.html', title = title)

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Welcome To OneMinutePitch!!!'
    return render_template('index.html',message = message)

@app.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View pitch page function that returns the movie details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)
