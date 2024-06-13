from flask import Flask, render_template, redirect
from loginForm import LoginForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "gobbledygook"
bs = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    formLogin = LoginForm()
    if formLogin.validate_on_submit():
        print(formLogin.email.data)
        if (formLogin.email.data == 'admin@email.com'
            and formLogin.password.data == '12345678'):
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template('login.html', form=formLogin)

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
