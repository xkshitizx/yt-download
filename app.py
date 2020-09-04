import webbrowser
import os
from dotenv import load_dotenv

from flask import Flask,render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField

from download import mp3_download


load_dotenv()


app = Flask(__name__)
app.config['DEBUG'] = False
app.config["SECRET_KEY"]: str = os.getenv("APP_SECRET")


class DownloadForm(FlaskForm):
    """Form to take url as an input"""
    url = StringField('Url')



@app.route('/',methods=['GET', 'POST'])
def index():
    form = DownloadForm()

    if form.validate_on_submit():
        return render_template("downloading.html", url=form.url.data, func=mp3_download)

    return render_template("index.html", form=form)

if __name__ == '__main__':
    app.run()