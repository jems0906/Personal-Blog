
from flask import Flask, render_template, abort, request, redirect, url_for, session
import article_storage

app = Flask(__name__)
app.secret_key = 'change_this_secret_key'  # Needed for session

# --- Basic Auth ---
ADMIN_USER = 'admin'
ADMIN_PASS = 'password'

def is_logged_in():
    return session.get('logged_in')

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_logged_in():
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# --- Guest Section ---
@app.route("/")
def home():
    articles = article_storage.list_articles()
    return render_template("home.html", articles=articles)

@app.route("/article/<article_id>")
def article(article_id):
    art = article_storage.get_article(article_id)
    if not art:
        abort(404)
    return render_template("article.html", article=art)

# --- Admin Section ---
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] == ADMIN_USER and request.form['password'] == ADMIN_PASS:
            session['logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            error = "Invalid credentials."
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route("/admin")
@login_required
def admin_dashboard():
    articles = article_storage.list_articles()
    return render_template("admin.html", articles=articles)

@app.route("/admin/new", methods=["GET", "POST"])
@login_required
def new_article():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        date = request.form['date'] or None
        import uuid
        article_id = str(uuid.uuid4())
        article_storage.save_article(article_id, title, content, date)
        return redirect(url_for('admin_dashboard'))
    return render_template("edit_article.html", article=None)

@app.route("/admin/edit/<article_id>", methods=["GET", "POST"])
@login_required
def edit_article(article_id):
    art = article_storage.get_article(article_id)
    if not art:
        abort(404)
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        date = request.form['date'] or art['date']
        article_storage.save_article(article_id, title, content, date)
        return redirect(url_for('admin_dashboard'))
    return render_template("edit_article.html", article=art)

@app.route("/admin/delete/<article_id>")
@login_required
def delete_article(article_id):
    article_storage.delete_article(article_id)
    return redirect(url_for('admin_dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
