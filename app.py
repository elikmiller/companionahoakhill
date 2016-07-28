# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/our_services')
def our_services():
	return render_template('our_services.html')

@app.route('/our_staff')
def our_staff():
	return render_template('our_staff.html')

@app.route('/contact_us')
def contact_us():
	return render_template('contact_us.html')

# start the server
if __name__ == '__main__':
	app.run(debug=True)