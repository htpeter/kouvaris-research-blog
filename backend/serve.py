from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("./homepage.html")


@app.route("/posts/model_monitoring")
def model_monitoring_post():
    return render_template("./posts/model_monitoring.html")


if __name__ == "__main__":
    app.run(debug=True)
