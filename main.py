from flask import Flask, render_template, redirect, url_for, flash
from forms import LoginForm
from google.cloud import datastore 


app = Flask(__name__)
posts = [
    {
        'author':'kyle',
        'title': 'frist blog',
        'content': 'Something about this bog is cool',
        'date_posted': 'April 20, 2018'   
    },
    {
        'author':'gevin',
        'title': 'second blog',
        'content': 'Something  cool',
        'date_posted': 'April 21, 2018'   
    },
]

app.config['SECRET_KEY'] = 'any secret string'
# user = users.get_current_user()

@app.route("/")
def hello():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'about')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #flash('User {} password {}'.format(form.email.data, form.password.data))
        return redirect(url_for('hello'))
    return render_template('login.html', title='Login', form=form)
    # if user:
    #     nickname = user.nickname()
    #     logout_url = users.create_logout_url('/')
    #     return 'Welcome, {}! (<a href="{}">sign out</a>)'.format(nickname, logout_url)
    # else:
    #     login_url = users.create_login_url('/')
    #     return '<a href="{}">Sign in</a>'.format(login_url)

@app.route("/register", methods=['GET', 'POST'])
def reg():
    form = LoginForm()
    if form.validate_on_submit():
        #flash('User {} password {}'.format(form.email.data, form.password.data))
        return redirect(url_for('hello'))
    return render_template('reg.html', title='reg', form=form)
    # if user:
    #     nickname = user.nickname()
    #     logout_url = users.create_logout_url('/')
    #     return 'Welcome, {}! (<a href="{}">sign out</a>)'.format(nickname, logout_url)
    # else:
    #     login_url = users.create_login_url('/')
    #     return '<a href="{}">Sign in</a>'.format(login_url)


if __name__ == '__main__':
    app.run(debug=True)