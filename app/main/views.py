from flask import render_template,request,redirect,url_for,abort
# from app import app
from ..models import Comment, User, Pitch
from .. import db,photos
from . import main
from flask_login import login_required
from .forms import UpdateProfileForm, InterviewForm
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
@login_required
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


    @main.route('/user/<uname>')
    def profile(uname):
        '''
        views
        '''
        user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html')


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


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

@main.route('/interview', methods = ["GET","POST"])
def Interview():
    form = InterviewForm()
    if form.validate_on_submit():
        interview = form.body.data 
        db.session.add(interview_pitch)
        db.session.commit()
        flash('Your pitch is already created')
        return redirect(url_for('main.new_pitch'))
    # title = "Create a pitch"
    pitches = Pitch.query.all()
    comments = Comment.query.all()
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('interview.html',form =form, interview_data =pitches )

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
