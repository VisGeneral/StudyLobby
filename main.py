from website import create_app
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import render_template, redirect, url_for,flash
app = create_app()
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per second"],
    storage_uri="memory://",
)
@app.errorhandler(404)
def nopage(e):
    flash('Page not found', category='error')
    return redirect(url_for('views.homepage'))
  #return render_template("404.html")
@app.errorhandler(403)
def nopermission(e):
  return render_template("403.html")
@app.errorhandler(429)
def toomanyrequests(e):
  return render_template("429.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 1234, debug="true")
