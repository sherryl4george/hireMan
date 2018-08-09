import os
class Config(object):
    SECRET_KEY = '$29000$N2YMIWQsBWBMae09x1jrPQ$1t8iyB2A.WF/Z5JZv.lfCIhXXN33N23OSgQYThBYRfk'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = '$29000$N2YMIWQsBWBMae09x1jrPQ$1t8iyB2A.WF/Z5JZv.lfCIhXXN33N23OSgQYThBYRfk'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    UPLOADED_STUDENTFILES_DEST = ''.join([os.getcwd(), '\\studentFiles'])
    UPLOADED_PHOTOS_ALLOW = set(['xls', 'xlsx'])