from . import db

class Aadhaar(db.Model):
    aadhaarNo = db.Column(db.String(12),primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(100))
    publicKey = db.Column(db.String(42))
    mobileNo = db.Column(db.String(10))

    def __init__(self,aadhaarNo,name,address,publicKey,mobileNo):
        self.aadhaarNo = aadhaarNo
        self.name = name
        self.address = address
        self.publicKey = publicKey
        self.mobileNo = mobileNo    

