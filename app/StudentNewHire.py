from app.ObjectValidator import ObjectValidator

class StudentNewHire:
    def __init__(self,uin,name,email,dept,term,year,position,fte,stipend,bdate,edate,jd,orientation,odate,oloc,sname,
                 semail,sphone,rname,remail,rdate,waiver,proficiency,international):
        self.uin = uin
        self.name = name
        self.email = email
        self.department = dept
        self.term = term
        self.year = year
        self.position = position
        self.fte = fte
        self.stipend = stipend
        self.bdate = bdate
        self.edate = edate
        self.jd = jd
        self.sname = sname
        self.sphone = sphone
        self.semail = semail
        self.rname = rname
        self.remail = remail
        self.rdate = rdate
        self.orientation = orientation
        self.odate = odate
        self.oloc = oloc
        self.waiver = waiver
        self.proficiency = proficiency
        self.international = international
        self.cbc = False
        self.approved = True
        self.schema = {
                        'uin':{'type':'number','empty':False,'min':100000000,'max':999999999},
                        'name':{'type':'string','empty':False},
                        'email':{'type':'string','empty':False},
                        'department': {'type': 'string', 'empty': False},
                        'term': {'type': 'list', 'allowed':['Spring','Summer','Fall'],'empty': False},
                        'year': {'type': 'number', 'min':1753, 'max':9999, 'empty': False},
                        'position':{'type':'list','empty':False,'allowed':['GA','TA','RA','GH']},
                        'fte':{'type':'number','empty':False},
                        'stipend': {'type': 'float'},
                        'bdate':{'type':'date','empty':False},
                        'edate':{'type':'date','empty':False},
                         'jd':{'type':'string','empty':False},
                         'sname':{'type':'string','empty':False},
                         'sphone':{'type':'string','empty':False},
                         'semail':{'type':'string','empty':False},
                         'rname':{'type':'string','empty':False},
                         'remail':{'type':'string','empty':False},
                         'rdate':{'type':'date','empty':False},
                         'orientation':{'type': 'list', 'empty': False,'allowed':['None','Mandatory','Optional']},
                         'odate':{'type':'datetime'},
                         'oloc':{'type':'string'},
                         'waiver':{'type':'boolean','empty':False},
                         'proficiency':{'type':'boolean'},
                         'international':{'type':'boolean'}
                      }

    def validate(self):
        v = ObjectValidator(self.schema)
        if v.validate_object(self):
            return True
        else:
            print(v.errors)
            return False