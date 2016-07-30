from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about_us():
	return render_template('about_us.html')

@app.route('/our_services')
def our_services():
	return render_template('our_services.html')

@app.route('/our_staff')
def our_staff():
	return render_template('our_staff.html')

@app.route('/contact_us')
def contact_us():
	return render_template('contact_us.html')

@app.route('/base')
def base():
	return render_template('base.html')

if __name__ == '__main__':
	app.run(debug=True)