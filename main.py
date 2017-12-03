from flask import Flask, request, redirect, render_template 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("signup.html", title="User Signup")


@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify_pass']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    #check if input is valid

    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error = "Not a valid username"
    
    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "Not a valid password"

    if verify_pass == "":
        verify_error = "Not a valid password"
    elif verify_pass != password:
            verify_error = "Password do not match"

    if email != "":
        if len(email) < 3 or len(email) > 20:
            email_error = "Not a valid email"

        if "." not in email or "@" not in email:
            email_error = "Not a valid email"

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", username=username)
    else:
        return render_template("signup.html", username_error=username_error, password_error=password_error, verify_error=verify_error,email_error=email_error,
                               username=username, email=email)

app.run()