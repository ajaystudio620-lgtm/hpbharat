from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "GASHPBHARAT_KEY"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        mobile = request.form.get("mobile")
        password = request.form.get("password")

        if mobile and password:
            session["user"] = mobile
            return redirect("/")

    return render_template("login.html")



@app.route("/logout")
def logout():

    session.clear()
    return redirect("/")



@app.route("/booking")
def booking():

    return render_template("booking.html")



@app.route("/tracking")
def tracking():

    return render_template("tracking.html")



@app.route("/services")
def services():

    return render_template("services.html")



@app.route("/contact")
def contact():

    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)