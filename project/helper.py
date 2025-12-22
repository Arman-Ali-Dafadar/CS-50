import requests

from flask import redirect, render_template, session
from functools import wraps



def login_required(f):
    """check if the user is logged in or not"""
    @wraps(f)
    def check_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return check_function

def get_books(query):
    """Uses the open library(openlibrary.org) API to get the
    desired data to be used"""
    url = ("https://openlibrary.org/search.json")
    response = requests.get(url, params={"q":query})
    data = response.json().get("docs",[])

    books = []

    for book in data:
        books.append({
            "title":book.get("title", "Unknown"),
            "author_name":book.get("author_name", ["Unknown"])[0],
            "year":book.get("first_publish_year", "Unknown"),
            "cover_id":book.get("cover_i"),
            #Use of the cover API in the openlibrary
            "cover_src":f"https://covers.openlibrary.org/b/id/{book.get('cover_i')}-M.jpg",
            "work_key":book.get("key")
            })

    return books

def book_info(work_key):
    """Get book info from OpenLibrary's works endpoint."""
    # Ensure the key does not start with a slash
    if isinstance(work_key, dict):
        work_key = work_key.get("work_key")
    work_key = work_key.lstrip("/")
    url = f"https://openlibrary.org/{work_key}.json"
    response = requests.get(url)
    if response.status_code != 200:
        return display_error("Invalid work key or request failed")

    data = response.json()
    # Title is always safe
    title = data.get("title")
    # Handle covers safely
    covers = data.get("covers", [])
    cover_src = None
    if covers:
        cover_src = f"https://covers.openlibrary.org/b/id/{covers[0]}-M.jpg"
    return {
        "title": title,
        "cover_src": cover_src,
        "work_key": f"/{work_key}"
    }



def display_error(message):
    """Display the meme using the memegen API
    Githud link - https://github.com/jacebrowning/memegen"""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("display_error.html", message=escape(message))
