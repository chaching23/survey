from flask import Flask, render_template, request, redirect, session, flash
from mysqlconn import connectToMySQL


app = Flask(__name__)
app.secret_key ='keep it safe'

print(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('mydb')
    survey = mysql.query_db('SELECT * FROM survey;')
    print(survey)
    return render_template("index.html", all_users= survey)


            
@app.route('/users', methods=['POST'])
def create_user():
    is_valid = True		
    if len(request.form['name']) < 1:
        is_valid = False
        flash("sorry")
    if len(request.form['email']) < 1:
        is_valid = False
        flash("sorry")
    if len(request.form['location']) < 1:
        is_valid = False
        flash("sorry")
    if len(request.form['language']) < 1:
        is_valid = False
        flash("sorry")
    if not is_valid:
        return redirect("/")
    else:
        mysql = connectToMySQL('mydb')
        query = "INSERT INTO users (name, email, location, language) VALUES (%(n)s, %(em)s, %(lo)s,%(la)s);"
        data = {
            "n": request.form["name"],
            "em": request.form["email"],
            "lo": request.form["location"],
            "la": request.form["language"]
            
            }

        db = connectToMySQL("mydb")
        db.query_db(query,data) 
        flash("Successfully Added!")
   
    return redirect("/show")


@app.route('/show')
def index2():
    mysql = connectToMySQL('mydb')
    survey = mysql.query_db('SELECT * FROM survey;')
    print(survey)
    return render_template("show.html", all_users= survey)



if __name__=="__main__":
    app.run(debug=True)

