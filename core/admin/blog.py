from arrow import now
from flask import Blueprint, flash, render_template, request, url_for, redirect
from flask_login import current_user, login_required

from core.forms.BlogPostForm import BlogPostForm
from core.models.BlogPost import BlogPost
from core import db

admin_blog = Blueprint('blog_admin', __name__)

@admin_blog.route('/new', methods=['POST', 'GET'])
@login_required
def new():
    form = BlogPostForm(request.form)
    if 'POST' == request.method and form.validate():
        post = BlogPost(
            name = form.name.data,
            content=form.content.data
        )
        post.user_id = current_user.id

        db.session.add(post)
        db.session.commit()
        flash('Post created successfully', 'success')

        return redirect(url_for('blog_admin.new'))

    return render_template('admin/blog/new.html', form=form, edit=False)


@admin_blog.route('/<int:id>/edit', methods=['POST', 'GET'])
@login_required
def edit(id: int):
    blog = BlogPost.query.one_or_404(id)

    if None == blog:
        flash(f'Blog with ID {id} not found', 'warning')
        return redirect(url_for('blog.index'))

    form = BlogPostForm(request.form, blog)
    if 'POST' == request.method and form.validate():
        blog.updatedAt = now().datetime
        blog.name = form.name.data
        blog.content = form.content.data

        db.session.commit()
        flash('Post edited successfully', 'success')

        return redirect(url_for('blog.index'))

    return render_template('admin/blog/new.html', form=form, edit=True)


@admin_blog.route('/<int:id>/delete')
@login_required
def delete(id):
    blog = BlogPost.query.get(id)

    if None == blog:
        flash(f'Blog with ID {id} not found', 'warning')
        return redirect(url_for('blog.index'))

    db.session.delete(blog)
    db.session.commit()

    flash(f'Blog post ID {id} deleted successfully', 'success')

    return redirect(url_for('blog.index'))
