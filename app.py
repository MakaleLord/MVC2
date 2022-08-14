#!/usr/bin/python3

from flask import Flask, render_template, abort
from .post.py import blog_posts
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('page.html', posts=blog_posts)

@app.route('/<post_link>')
def post_page(post_link):
    for post in blog_posts:
        if post['permalink'] == post_link:
            return render_template('post.html', post=post)
        abort(404)
