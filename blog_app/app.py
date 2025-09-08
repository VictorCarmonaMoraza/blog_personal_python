from flask import Flask, render_template

from Data import data

app = Flask(__name__)


@app.route('/')
def home():
    posts = data.posts
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
