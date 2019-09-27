from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import EntryForm
from app.models import PostForm

@app.route('/')
def index():
    post_work = PostForm.query.filter_by(category='w').all()
    post_personal = PostForm.query.filter_by(category='p').all()
    path = request.path
    return render_template('index.html', post_work=post_work, post_personal=post_personal, path=path)

@app.route('/new/task/', methods=['GET', 'POST'])
def new_task():
    form = EntryForm()
    if form.validate_on_submit():
        new_post = PostForm(title=form.title.data,
                            category=form.category.data,
                            task=form.task.data)
        db.session.add(new_post)
        db.session.commit()
        flash('Task added to ToDo List', 'success')
        return redirect(url_for('index'))
    path = request.path
    return render_template('new_task.html', title='Add Task', form=form, path=path)

@app.route('/modify/<int:post_id>/', methods=['GET', 'POST'])
def modify(post_id):
    form = EntryForm()
    mod_post = PostForm.query.get(post_id)
    if form.validate_on_submit():
        mod_post.title = form.title.data
        mod_post.category = form.category.data
        mod_post.task = form.task.data
        db.session.commit()
        flash('ToDo List was Modified', 'success')
        return redirect(url_for('index'))
    else:   
        if not mod_post:
            flash('No post with that ID', 'warning')
            return redirect(url_for('index'))
        else:
            form.title.data = mod_post.title
            form.category.data = mod_post.category
            form.task.data = mod_post.task
            return render_template('modify.html', title='Modify Task', form=form, post_id=post_id)

@app.route('/delete/<int:post_id>/', methods=['GET', 'POST'])
def del_post(post_id):
    del_post = PostForm.query.get(post_id)
    db.session.delete(del_post)
    db.session.commit()
    flash('Post Deleted', 'success')
    return redirect(url_for('index'))

