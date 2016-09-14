from flask import Flask, render_template, send_from_directory, redirect, url_for

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

@app.route('/attachments/<filename>')
def download_file(filename):
	return redirect('static/attachments/' + filename)

if __name__ == '__main__':
	app.run(debug=True)
