# HERE WE GONNA DEFINE OUR FORMS IN ORDER TO GET DATA FOR OUR USERS

# FIRST AT ALL WE NEED TO IMPORT WTF IN ORDER TO UDE FORMS AND ALSO WE GONNA NEED DATA VALIDATORS
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_pagedown.fields import PageDownField



# WE CREATE A CLASS IN ORDER TO CREATE OUR FIRST FORM

class PostForm(FlaskForm):
    body = PageDownField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = StringField('Enter your comment', validators=[Required()])
    submit = SubmitField('Submit')

