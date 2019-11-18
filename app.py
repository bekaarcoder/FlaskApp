from project import app
from flask import render_template
from project.models import Task

@app.route('/')
def index():
    all_tasks = Task.query.all()
    return render_template('index.html', all_tasks=all_tasks)

if __name__ == '__main__':
    app.run(debug=True)
