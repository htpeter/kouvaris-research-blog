from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("./homepage.html")


@app.route("/posts/model_monitoring")
def model_monitoring_post():
    return render_template("./posts/model_monitoring.html")


@app.route("/posts/tiered_open_education")
def tiered_open_education():
    return render_template("./posts/tiered_open_education.html")


if __name__ == "__main__":
    app.run(debug=False)
