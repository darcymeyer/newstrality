from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import requests
import urllib
from bs4 import BeautifulSoup
from readability.readability import Document # https://github.com/buriy/python-readability. Tried Goose, Newspaper (python libraries on Github). Bad results.
from http.cookiejar import CookieJar #

from newspaper import Article

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'newstrality'

class UrlForm(Form):
    url = TextField('Enter article URL to calculate newstrality:', validators=[validators.required()])
    submit = SubmitField('Calculate')

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = UrlForm(request.form)
    if request.method == 'POST':
        url=request.form['url']
        print(url)
        if form.validate():
            print(url)
            return redirect(url_for('view', url=url))
    return render_template('index.html', form=form)

@app.route('/view/<path:url>')
def view(url):
    title = ""
    authors = ""
    publish_date = ""
    text = ""
    top_image = ""
    try:
        # opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)
        # opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7')]
        # html =  opener.open(url).read().decode('utf-8')
        # readable_article = Document(html).summary()
        # soup = BeautifulSoup(readable_article, "lxml")
        # text = soup.get_text()
        article = Article(url)
        article.download()
        article.parse()

        title = article.title
        authors = article.authors
        publish_date = article.publish_date
        text = article.text
        top_image = article.top_image
    except:
        title = "error"
        text = "error"
        authors = "error"
        publish_date = "error"
        top_image = "error"
    return render_template('view.html', title = title, authors = authors, publish_date=publish_date, text=text, top_image=top_image)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
