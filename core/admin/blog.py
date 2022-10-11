from datetime import datetime
from flask import Blueprint, flash, render_template, request, url_for, redirect
from flask_login import current_user
from werkzeug.utils import secure_filename

from core.decorators.is_granted import is_granted
from core.forms.BlogPostForm import BlogPostForm
from core.models.BlogPost import BlogPost
from core import db
from core.services.file_upload import upload_for_blog

admin_blog = Blueprint('blog_admin', __name__)


@admin_blog.route('/', methods=['GET'])
@is_granted('ROLE_ADMIN')
def list():
    blogs = BlogPost.query.all()

    return render_template('admin/blog/index.html', blogs=blogs)

@admin_blog.route('/new', methods=['POST', 'GET'])
@is_granted('ROLE_ADMIN')
def new():
    form = BlogPostForm(request.form)
    if 'POST' == request.method and form.validate():
        filename = upload_for_blog(request.files['image'])

        post = BlogPost(
            name = form.name.data,
            content=form.content.data
        )
        post.user_id = current_user.id
        post.image = filename

        db.session.add(post)
        db.session.commit()
        flash('Post created successfully', 'success')

        return redirect(url_for('blog_admin.new'))

    return render_template('admin/blog/new.html', form=form, edit=False)


@admin_blog.route('/<int:id>/edit', methods=['POST', 'GET'])
@is_granted('ROLE_ADMIN')
def edit(id: int):
    blog = BlogPost.query.get(id)

    if None == blog:
        flash(f'Blog with ID {id} not found', 'warning')
        return redirect(url_for('blog.index'))

    form = BlogPostForm(request.form, blog)
    if 'POST' == request.method and form.validate():
        f = request.files['image']

        if f:
            filename = upload_for_blog(f)
            blog.image = filename

        blog.updatedAt = datetime.now()
        blog.name = form.name.data
        blog.content = form.content.data

        db.session.commit()
        flash('Post edited successfully', 'success')

        return redirect(url_for('blog.index'))

    return render_template('admin/blog/new.html', form=form, edit=True)


@admin_blog.route('/<int:id>/delete')
@is_granted('ROLE_ADMIN')
def delete(id):
    blog = db.get_or_404(BlogPost, id)

    db.session.delete(blog)
    db.session.commit()

    flash(f'Blog post ID {id} deleted successfully', 'success')

    return redirect(url_for('blog.index'))
