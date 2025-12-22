from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helper import display_error, login_required, get_books, book_info

app = Flask(__name__)

app.secret_key = "FAY4O87AVFIY4OQ84OUVLILAVJGNSJKVL74Y94853QH473HQVW"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///final_project.db")

@app.route("/")
@login_required
def index():
    popular_books = get_books("popular")[:10]
    self_help_books = get_books("self help")[:10]
    political_books = get_books("political")[:10]
    space_books = get_books("space")[:10]
    science_books = get_books("science")[:10]
    return render_template("index.html", popular_books=popular_books,
    self_help_books=self_help_books,political_books=political_books,
    space_books=space_books,scince_books=science_books)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        session.clear()
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return display_error("MUST PROVIDE USERNAME")

        if not password:
            return display_error("MUST PROVIDE PASSWORD")

        rows = db.execute("SELECT * FROM user WHERE username=?;", username)

        if len(rows)!=1:
            return display_error("USER NOT FOUND")
        if not check_password_hash(rows[0]["hash"], password):
            return display_error("INVALID PASSWORD")

        session["user_id"]=rows[0]["id"]

        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/register", methods=("GET","POST"))
def register():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not username or not password or not confirm_password:
            return display_error("INVALID INPUT")
        if password!=confirm_password:
            return display_error("PASSWORD NOT MATCH")
        rows = db.execute("SELECT * FROM user WHERE username=?;",username)
        if len(rows) != 0:
            return display_error("USERNAME NOT AVAILABLE")
        hash = generate_password_hash(password)
        db.execute("INSERT INTO user (username,hash) VALUES (?,?);",username,hash)
        return redirect("/login")
    else:
        return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")


@app.route("/search", methods=("GET","POST"))
@login_required
def search():
    query = request.form.get("query")
    if not query:
        return display_error("NO QUERY ENTERED")
    query_books=get_books(query)
    return render_template("search.html",query=query,query_books=query_books)

@app.route("/password", methods=("GET","POST"))
@login_required
def password():
    if request.method=="POST":
        current_password=request.form.get("password")
        new_password=request.form.get("new_password")
        confirm_password=request.form.get("confirm_password")
        if not current_password or not new_password or not confirm_password:
            return display_error("INVALID INPUT")
        user_id=session["user_id"]
        rows = db.execute("SELECT * FROM user WHERE id=?;", user_id)
        hashed_password = rows[0]["hash"]
        if not check_password_hash(hashed_password, current_password):
            return display_error("INCORRECT PASSWORD")
        if new_password!=confirm_password:
            return display_error("NEW PASSWORD NOT MATCH")
        db.execute("UPDATE user SET hash=? WHERE id=?;",generate_password_hash(new_password),user_id)
        session.clear()
        return redirect("/")
    else:
        return render_template("password.html")

@app.route("/bookmarks", methods=("GET","POST"))
@login_required
def bookmarks():
    if request.method=="POST":
        user_id=session["user_id"]
        title=request.form.get("title")
        author=request.form.get("author")
        cover_src=request.form.get("cover_src")
        work_key=request.form.get("work_key")
        check_result=db.execute("SELECT * FROM bookmarks WHERE user_id=? AND work_key=?;",user_id, work_key)
        if not len(check_result)==0:
            return display_error("ALREADY BOOKMARKED")
        db.execute("INSERT INTO bookmarks(user_id,title,author,cover_src,work_key) VALUES(?,?,?,?,?)",user_id,title,author,cover_src,work_key)
        return redirect("/bookmarks")
    else:
        user_id=session["user_id"]
        bookmarked_books=db.execute("SELECT work_key FROM bookmarks WHERE user_id=?;",user_id)
        books_info = []
        for book in bookmarked_books:
            info = book_info(book)
            books_info.append(info)
        return render_template("bookmarks.html",books_info=books_info)


@app.route("/delete", methods=("GET","POST"))
@login_required
def delete():
    if request.method=="POST":
        user_id=session["user_id"]
        work_key=request.form.get("work_key")
        rows = db.execute("SELECT * FROM bookmarks WHERE user_id=? AND work_key=?;",user_id,work_key)
        if len(rows)==0 or len(rows)>1:
            return display_error("INVALID")
        db.execute("DELETE FROM bookmarks WHERE user_id=? AND work_key=?",user_id,work_key)
        return redirect("/bookmarks")
