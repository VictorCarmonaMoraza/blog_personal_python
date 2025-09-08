from flask import Flask, render_template

app = Flask(__name__)

#Static Route
@app.route('/')
def home():
    return render_template('index.html', title='Bienvenido a mi sitio Web')

# Dynamic Route
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Displaying Post #{post_id}"

if __name__ == "__main__":
    app.run(debug=True)