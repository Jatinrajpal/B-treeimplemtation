from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, SearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'dairy_name': 'sl dairy',
        'title': 'PANNER',
        'content': 'id-1',
        'date_posted': 'April 20, 2020'
    },
    {
        'dairy_name': 'sri lakshmi dairy',
        'title': 'MILK',
        'content': 'id-2',
        'date_posted': 'April 21, 2020'
    },
    {
        'dairy_name': 'sl dairy',
        'title': 'GHEE',
        'content': 'id-3',
        'date_posted': 'April 20, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    return render_template('search.html', title='search', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('register'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
