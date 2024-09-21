from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .utils import load_tasks, save_tasks
from .models import Task

tasks = Blueprint('tasks', __name__)


@tasks.route('/')
def list_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    user_tasks = load_tasks(session['user'])

    return render_template('tasks.html', tasks=user_tasks)


@tasks.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    title = request.form['title']
    description = request.form['description']
    new_task = Task(title, description)
    user_tasks = load_tasks(session['user'])
    user_tasks.append(new_task)

    save_tasks(session['user'], user_tasks)

    flash('Task added successfully.', 'success')

    return redirect(url_for('tasks.list_tasks'))

@tasks.route('/complete/<int:task_index>')
def complete_task(task_index):
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    user_tasks = load_tasks(session['user'])

    if 0 <= task_index < len(user_tasks):
        user_tasks[task_index].completed = True
        save_tasks(session['user'], user_tasks)
        flash('Task marked as complete.', 'success')
    else:
        flash('Invalid task.', 'error')

    return redirect(url_for('tasks.list_tasks'))

@tasks.route('/delete/<int:task_index>')
def delete_task(task_index):
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    user_tasks = load_tasks(session['user'])

    if 0 <= task_index < len(user_tasks):
        del user_tasks[task_index]
        save_tasks(session['user'], user_tasks)
        flash('Task deleted successfully.', 'success')
    else:
        flash('Invalid task.', 'error')

    return redirect(url_for('tasks.list_tasks'))
