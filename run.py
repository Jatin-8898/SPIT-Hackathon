from app import app, totp, sock
from app.models import Aadhaar
from flask import render_template, session,request,url_for,redirect


@app.route("/",methods=['GET','POST'])
def index():
	if(request.method == "POST"):
		aadhaarNo = request.form['aadhaarNo']
		session['currentUser'] = aadhaarNo
		return redirect(url_for('stock'))
		
	return render_template("index.html")


@app.route("/getUsage")
def getUsage():
    return render_template("getUsage.html")


@app.route("/sendOtp")
def sendOtp():
    beneficiary = Aadhaar.query.get(session['currentUser'])

    otp = totp.now()
    session['OTP'] = otp
    string = "{phone_no:"+beneficiary.mobileNo+",OTP:"+otp+"}"
    stringToSend = ((string)+"\n")
    sock.send(stringToSend.encode())
    return "True"


@app.route("/verifyOtp/<string:otp>")
def verifyOtp(otp):
    if session['OTP'] == otp:
        return "True"
    else:
        return "False"


@app.route("/stock")
def stock():
	return render_template("stock.html")


@app.route("/supplier")
def supplier():
    return render_template("supplier.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
