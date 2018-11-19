from flask import render_template
# from app import app
from .. import db
from . import main
from flask_login import login_required
# from ..models import comments
# from .forms import CommentForm
# Comment = comment.Comment

def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to One-Minute-Pitch Website Online'
    return render_template('index.html', title = title)

# Views
@main.route('/')
def index():

    

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Welcome To OneMinutePitch!!!'
    print(message)
    return render_template('index.html',message = message)


@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):


@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)

@main.route('/pickup')
def pickup():

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('pickup.html')

@main.route('/interview')
def interview():
    
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('interview.html')

@main.route('/product')
def product():
    
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('product.html')


@main.route('/promotion')
def promotion():
    
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('promotion.html')

   



# @main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
# def new_comment(id):
#     form = CommentForm()
#     pitch = get_pitch(id)
