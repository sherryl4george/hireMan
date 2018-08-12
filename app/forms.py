from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField,BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

from app import files
class BulkUploadForm(FlaskForm):
    file = FileField(validators=[FileAllowed(files, 'Excel files only!'), FileRequired('File was empty!')])
    check = BooleanField('Confirm Upload?', validators=[DataRequired()])
    submit = SubmitField('Upload')