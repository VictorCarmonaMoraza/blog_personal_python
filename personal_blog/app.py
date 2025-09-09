from flask import Flask, render_template

## from personal_blog.dataTest.dataPost import posts
from dataTest.dataPost import posts



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts = posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post =next((post for post in posts if post['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return "<h1>Post not found</h1>", 404


if __name__ == "__main__":
    app.run(debug=True)