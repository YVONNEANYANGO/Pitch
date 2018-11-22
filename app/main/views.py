from flask import render_template,request,redirect,url_for,abort
# from app import app
from ..models import Comment, User, Pitch
from .. import db,photos
from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfileForm, InterviewForm,PromotionForm,PickupForm,ProductForm
# from ..models import Comments
from .forms import CommentForm
# Comment = comment.Comment

def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to One-Minute-Pitch Website Online'
    return render_template('index.html', title = title)

# ViewC
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


@main.route('/comment/<pitch_id>', methods = ["GET","POST"]) 
def comment(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.body.data
        new_comment = Comment(comment = comment, pitch = pitch)
        db.session.add(new_comment)
        db.session.commit()

    return render_template('comment.html',comment_form =  comment_form)

@main.route('/pickup', methods = ["GET","POST"])
def pickup():
    form = PickupForm()
    if form.validate_on_submit():
        pickup = form.body.data
        pitch = Pitch(description = pickup, user = current_user, category = "pickup")
        db.session.add(pitch)
        db.session.commit()
        # flash('Your pitch is already created')
        # return redirect(url_for('main.pitch'))

    pitches = Pitch.query.filter_by(category = "pickup")
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('pickup.html', form = form, pickup_data = pitches)

@main.route('/interview', methods = ["GET","POST"])
def Interview():
    form = InterviewForm()
    if form.validate_on_submit():
        interview = form.body.data 
        pitch = Pitch(description = interview, user = current_user, category = "interview")
        db.session.add(pitch)
        db.session.commit()
        # flash('Your pitch is already created')
    # title = "Create a pitch"
    pitches = Pitch.query.filter_by(category = "interview")
    
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('interview.html',form =form, interview_data =pitches)

@main.route('/product', methods = ["GET","POST"])
def product():
    form = ProductForm()
    if form.validate_on_submit():
        product = form.body.data
        pitch = Pitch(description = product, user = current_user, category = "product")
        db.session.add(pitch)
        db.session.commit()
        # flash('Your pitch is already created')
        # return redirect(url_for('main.pitch'))

    pitches = Pitch.query.filter_by(category = "product")
    
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('product.html', form = form, product_data = pitches)

@main.route('/promotion', methods = ["GET","POST"])
def promotion():
    form = PromotionForm()
    if form.validate_on_submit():
        promotion = form.body.data
        pitch = Pitch(description = promotion, user = current_user, category = "promotion")
        db.session.add(pitch)
        db.session.commit()
        # flash('Your pitch is already created')
        # return redirect(url_for('main.pitch'))

    pitches = Pitch.query.filter_by(category = "promotion")
    
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('promotion.html', form = form, promotion_data = pitches)
@main.route("/view/comments/<pitch_id>")
def view_comments(pitch_id):

    comments = Comment.query.filter_by(pitch_id = pitch_id)

    return render_template("view_comments.html", comments = comments)
# # comment-section
# @main.route('/comments/<int:id>', methods=['GET','POST']



