from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)


UPLOAD_FOLDER = 'static/'
language='en'
app.secret_key = "secret key"

@app.route('/uploaddoc',methods=['GET','POST'])
def hello():
    print(session)
    if "logged_in" in session:
         return render_template('upload-document.html')
    else:
        return redirect('/')

@app.route('/documents')
def helo():
    if "logged_in" not in session:
        return render_template('documents-page.html')
    else:
        return redirect('/')

@app.route('/search')
def doc():
    if "logged_in" in session:
        return render_template('search-or-uploading-page.html')
    else:
        return redirect('/')


@app.route("/")
def one():
    return render_template('login.html')



@app.route("/", methods=["GET", "POST"])
def login():
    print(request.method)
    if request.method == "POST":
        print(request.form.get("email"))
        if request.form.get("email") == 'admin@gmail.com' and request.form.get("pwd") =='admin' :
            print('gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg')
            session['logged_in'] = True
            session['email']=request.form.get("email")

            return redirect('/uploaddoc')

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")




if __name__ == '__main__':
    app.run()
