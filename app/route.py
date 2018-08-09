import os, uuid

from flask import render_template
from flask_security import login_required,current_user
from werkzeug.utils import secure_filename
from werkzeug import FileStorage


from app import app
from app.forms import BulkUploadForm
from app import files


from app import utils

@app.route('/bulkupload', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
@login_required
def bulkupload():
    form = BulkUploadForm()
    if form.validate_on_submit():
        # print(form.file)
        _, file_extension = os.path.splitext(secure_filename(form.file.data.filename))
        temp = ''.join([uuid.uuid4().hex,file_extension])
        filename = files.save(FileStorage(form.file.data),name=secure_filename(temp))
        file_url = files.url(filename)
        utils.process_bulkupload(filename,file_url)
        return render_template('base.html')
    return render_template('bulkupload.html', title='New Hire - Bulk Upload', form=form)
