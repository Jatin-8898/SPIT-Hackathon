from app import app, totp
import socket
from app.models import *
from flask import render_template, session,request,url_for,redirect,flash
import requests

@app.route("/",methods=['GET','POST'])
def index():
	if(request.method == "POST"):
		aadhaarNo = request.form['aadhaarNo']
		session['currentUser'] = aadhaarNo
		user = Aadhaar.query.get(aadhaarNo)
		entitlement = Entitlement.query.get(user.category)
		if user.category == "GEN":
			session['maxAmount'] = user.generalCount.count * entitlement.maxAmount
		else:
			session['maxAmount'] = entitlement.maxAmount

		return redirect(url_for('stock'))

	session.clear()
	return render_template("index.html")


@app.route("/getUsage")
def getUsage():
	user = Aadhaar.query.get(session['currentUser'])
	return render_template("getUsage.html",name=user.name)


@app.route("/sendOtp")
def sendOtp():
	beneficiary = Aadhaar.query.get(session['currentUser'])

	otp = totp.now()
	session['OTP'] = otp
	string = "{phone_no:"+beneficiary.mobileNo+",OTP:"+otp+"}"
	stringToSend = ((string)+"\n")
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(("192.168.43.223",6000))
	count = sock.send(stringToSend.encode())
	return redirect(url_for('stock'))


@app.route("/verifyOtp/<string:otp>")
def verifyOtp(otp):
    if session['OTP'] == otp:
        return "True"
    else:
        return "False"


@app.route("/stock",methods=['GET','POST'])
def stock():
	if(request.method == "POST"):
		total = int(request.form['riceQuantity']) + int(request.form['wheatQuantity']) + int(request.form['coarseQuantity'])
		session['rice'] = int(request.form['riceQuantity'])
		session['wheat'] = int(request.form['wheatQuantity'])
		session['coarse'] = int(request.form['coarseQuantity'])

		if(total > session['maxAmount']):
			flash("You are only allowed "+str(session['maxAmount'])+" KG")
			return redirect(url_for('stock'))
		else:
			flash("A message has been sent")
			return redirect(url_for("sendOtp"))

	return render_template("stock.html")


@app.route("/supplier")
def supplier():
    return render_template("supplier.html")


@app.route("/profile")
def profile():
	user = Aadhaar.query.get(session['currentUser'])
	return render_template("profile.html",aadhaarNo=user.aadhaarNo,name=user.name,address=user.address,mobileNo=user.mobileNo,category=user.category)


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
