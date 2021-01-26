from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    template_variables = {
        "page_nme": "@/",
        "pages": [
            {
                "page_name": "test page 1",
                "content": """
        Twoooooooooooo
        """,
            },
            {"page_name": "test page 2"},
        ],
    }
    return render_template("./homepage.html", **template_variables)


if __name__ == "__main__":
    app.run(debug=False)
