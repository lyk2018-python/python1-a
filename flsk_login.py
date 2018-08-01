from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'asd0212£$½#$¾#$½'

@app.route("/logout")
def logout():
    session.pop('loggedin')
    return redirect("/")

@app.route("/",methods=['GET','POST'])
def home():
    print(request.method)
    print(request.form)
    print(request.headers)

    if request.headers.get('User-Agent').lower().find('mozilla') == -1:
        return "İZİNSİZ"
    if request.method == 'POST':
        print(dict(request.form))
        if request.form.get('email') == 'xcoder@msn.com' and request.form.get('password') == 'mustafa':
            session['loggedin'] = 'asdasdasd'

    if session.get('loggedin', None) is None:
        return render_template("index.html")
    else:
        return render_template("hello.html")


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
