from . import db

class Aadhaar(db.Model):
    aadhaarNo = db.Column(db.String(12),primary_key=True)
    generalCount = db.relationship('GeneralCount',backref='user',uselist=False)
    name = db.Column(db.String(50))
    address = db.Column(db.String(100))
    publicKey = db.Column(db.String(42))
    mobileNo = db.Column(db.String(10))
    category = db.Column(db.String(3))

    def __init__(self,aadhaarNo,name,address,publicKey,mobileNo,category):
        self.aadhaarNo = aadhaarNo
        self.name = name
        self.address = address
        self.publicKey = publicKey
        self.mobileNo = mobileNo
        self.category = category

class GeneralCount(db.Model):
    aadhaarNo = db.Column(db.String(12),db.ForeignKey('aadhaar.aadhaarNo'),primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self,aadhaarNo,count):
        self.aadhaarNo = aadhaarNo
        self.count = count

class Entitlement(db.Model):
    category = db.Column(db.String(3),primary_key=True)
    maxAmount = db.Column(db.Integer)

    def __init__(self,category,maxAmount):
        self.category = category
        self.maxAmount = maxAmount



