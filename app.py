from flask import Flask ,render_template


app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/a1/api/login')
def user_login():
    return "login here"


@app.route('/a1/api/signup')
def signup():
    return "signup here"



@app.route('/a1/api/blog')
def blog():
    return "blog here"


if __name__=="__main__":
  app.run(debug=True)