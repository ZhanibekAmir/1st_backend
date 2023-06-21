from flask import Flask, render_template
app = Flask(__name__)



@app.route("/mainpage")
def main():
    return render_template('mainpage.html')

@app.route("/gallery")
def gallery():
    user = {
        "name" : "Amir",
        "age" : 14
    }
    return render_template('gallery.html',user=user)


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/index")
def index():
    user = {
        "name" : "Amir",
        "age" : 14
    }
    return render_template('index.html',user=user)


@app.route("/profile")
def profile():
    user = {
        "name": "Amir",
        "age": 14
}
    return render_template('profile.html',user=user)


if __name__ == "__main__":
    app.run(debug=True)



