
from flask import Blueprint, flash, render_template, url_for, redirect

from core.models.blog_post import BlogPost

blog = Blueprint('blog', __name__)

@blog.route('/', methods=['GET'])
def index():
    blogs = BlogPost.query.all()

    return render_template('blog/index.html', blogs=blogs)

@blog.route('/<int:id>/show')
def show(id: int):
    blog_post = BlogPost.query.get(id)
    if None is blog_post:
        flash(f'Blog with ID {id} not found', 'warning')
        return redirect(url_for('blog.index'))

    return render_template('blog/show.html', blog=blog_post)
