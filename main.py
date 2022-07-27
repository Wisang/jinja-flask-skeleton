from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"id": 1, "title": "This is the first title",
     "content": "This is first content"},
    {"id": 2, "title": "This is the second title",
     "content": "This is second content"},
    {"id": 3, "title": "This is the third title",
     "content": "This is third content"}
]


@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)


@app.route('/posts/<int:page>')
def get_posts(page):
    post = posts[page-1]
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
