from flask import Flask, url_for, request
from enums import RequestMethods

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi! Welcome to the Index Page"

@app.route('/hello')
def hello():
    return "Hello World~"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/login', methods=[RequestMethods.GET, RequestMethods.POST])
def login():
    if request.method == RequestMethods.POST:
        _login_user()
    else:
        _show_login_form()

def _login_user():
    return 'Logging in...'

def _show_login_form():
    return 'Please Login'

# test_request_context() gets flask to behave as if it were handling a request
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='John Doe'))

if __name__ == "__main__":
    app.run()
