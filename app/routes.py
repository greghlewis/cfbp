from app import app
from flask import render_template, session, flash, redirect, url_for
from app.forms import LoginForm

@app.route("/")
def home():
    x = session.get('x', None)

    if not x:
        session['x'] = 1
    elif x >= 10:
        session.clear()
        return 'Session Cleared'
    else:
        session['x'] = x + 1

    return "The number of refreshes is {}".format(str(session['x']))

@app.route("/hello/<name>")
def hello_name(name):
    return 'hello ' + name + "!"

# ------------ Factor tests ------------
def factors(num):
    return [x for x in range(1, num + 1) if num%x==0]

@app.route("/square/<int:num>")
def factors_num(num):
    return "The factors of {} are {}".format(num, tuple(factors(num)))

# @app.route("/html_test/<int:num>")
# def factors_html(num):
#     factor_list = factors(int(num))
#
#     html = "<h1> The factors of {} are <h1>".format(str(num))
#     html = html + "\n <ul>"
#     for f in factor_list:
#         html = html + "<li> {} </li>".format(f)
#     html = html + "</ul> </body>"
#
#     return html

@app.route("/template_test/<int:num>")
def factor_fancy(num):
    return render_template(
        "factors.html",
        number = num,
        factor_list = factors(num)
    )

@app.route("/welcome")
def hello():
    user = {'username':'Greg'}
    return render_template('index.html', user=user)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me ={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('hello'))
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0')