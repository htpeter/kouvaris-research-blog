from flask import Flask, render_template

app = Flask(__name__)

ROOT_PAGE = 'research-development'

@app.route("/")
def homepage():
    return render_template("./roam_notes/{0}-md.html".format(ROOT_PAGE))

@app.route("/r/<slug>")
def roam_template(**kwargs):
    # print(kwargs)
    return render_template("./roam_notes/{slug}-md.html".format(**kwargs))


@app.route("/posts/model_monitoring")
def model_monitoring_post():
    return render_template("./posts/model_monitoring.html")

@app.route("/landing")
def landing_page():
    return render_template("./landing/friend_fb_landing_page.html")


@app.route("/posts/tiered_open_education")
def tiered_open_education():
    return render_template("./posts/tiered_open_education.html")


if __name__ == "__main__":
    app.run(debug=False)
