from flask import Flask,render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import stories

app=Flask(__name__)

app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

#routes ==> homepage to display stories
@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/")
def homepage():
    return render_template("homepage.html", prompts=stories.story.prompts)

@app.route("/story", methods=["POST"])
def story():
    text = stories.story.generate(request.form)
    return render_template("story.html", text=text)