from flask import Flask, request, render_template 
app= Flask(__name__)
app.config['DEBUG'] = True
@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/",methods=["post"])
def math():
    username = request.form['username']
    password = request.form['password'] 
    verify = request.form['verify']
    email = request.form['email']
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error = "invalid username" 
    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "invalid password"
    if verify != password:
        verify_error = "Entries don't match"
    if email != "":
        if len(email) < 3 or len(email) > 20 or " " in email or email.count("@") != 1 or email.count(".") != 1:
            email_error = "invalid email"
    if  email_error or username_error or password_error or verify_error:  
        return render_template("index.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, name = username, email = email)
    else:
         return render_template("welcome.html",username = username)
    

app.run()
