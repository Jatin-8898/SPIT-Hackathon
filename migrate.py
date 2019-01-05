from app import db
from app.models import *

db.drop_all()
db.create_all()


sarvesh = Aadhaar("592036400388","Sarvesh Harale","5A Kedarnath","0xc5B4fFab89D58a55Ecc2181D1fB5A05bCf85F311","9967602289")
jatin = Aadhaar("123456789012","Jatin Varlyani","USA","0xc5B4fFab89D58a55Ecc2181D1fB5A05bCf85F311","7972731550")

db.session.add(sarvesh)
db.session.add(jatin)

db.session.commit()
