from flask import Blueprint, render_template, session, redirect, url_for
from .utils import load_tasks
import matplotlib

matplotlib.use('Agg')  # Set the backend to Agg (non-interactive)
import matplotlib.pyplot as plt
import io
import base64

data_viz = Blueprint('data_viz', __name__)


@data_viz.route('/data_viz')
def visualize_data():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    user_tasks = load_tasks(session['user'])
    completed_tasks = sum(1 for task in user_tasks if task.completed)
    incomplete_tasks = len(user_tasks) - completed_tasks

    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie([completed_tasks, incomplete_tasks], labels=['Completed', 'Incomplete'], autopct='%1.1f%%')
    plt.title('Task Completion Status')

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()  # Close the figure to free up memory

    # Encode the bytes buffer to base64
    image = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render_template('data_viz.html', image=image)