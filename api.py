from flask import Flask,render_template,request#looks inside the code for the html file.
app = Flask(__name__)#dunder-method

@app.route('/')#decorators #route hit
def home():#goes to the function
    return render_template('home.html')#return value will run the home.html file on webpage.


@app.route('/about')#decorators #route hit
def about():#goes to the function
    return render_template('about.html')#return value

@app.route('/contact')#decorators #route hit
def contact():#goes to the function
    return render_template('contact.html')#return value

@app.route('/login',methods=['POST'])#decorators #route hit
def login():#goes to the function
	user = {'username':'kittu', 'password':'saven'}#dictionary to which 
	username=request.form['username']
	password=request.form['password']

	if user['username']==username:
		if user['password']==password:
			return "login successful"
		return "password is wrong"
	return "username is wrong"


    


app.run(debug=True)#activating app in which Flask has been impoted with debug activated.