from flask import Flask, render_template

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

if __name__ == '__main__':
	app.run(debug=True)
