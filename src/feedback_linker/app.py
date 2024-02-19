"""App module."""
from __future__ import annotations

from typing import Union

from flask import Flask, flash, redirect, render_template, url_for
from werkzeug.wrappers.response import Response

from feedback_linker.forms import (
    FeedbackForm,
    LinkForm,
    LoginForm,
    PersonForm,
    ProjectForm,
)
from feedback_linker.models import (
    Feedback,
    Link,
    Person,
    Project,
    db,
    init_app,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback_linker.db'

init_app(app)


@app.route('/')
def index() -> str:
    """Define the view for the index page."""
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    """Define the view for managing login."""
    form = LoginForm()
    # Login logic here
    return render_template('login.html', form=form)


@app.route('/projects', methods=['GET', 'POST'])
def manage_projects() -> Union[Response, str]:
    """Define the view for managing projects."""
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data)
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!')
        return redirect(url_for('manage_projects'))
    projects = Project.query.all()
    return render_template('project_list.html', form=form, projects=projects)


@app.route('/people', methods=['GET', 'POST'])
def manage_people() -> str:
    """Define the view for managing people."""
    form = PersonForm()
    # Person creation logic here
    people = Person.query.all()
    return render_template('people_list.html', form=form, people=people)


@app.route('/links', methods=['GET', 'POST'])
def manage_links() -> str:
    """Define the view for managing links."""
    form = LinkForm()
    # Link creation logic here
    links = Link.query.all()
    return render_template('link_list.html', form=form, links=links)


@app.route('/feedback', methods=['GET', 'POST'])
def submit_feedback() -> str:
    """Define the view for submitting feedback."""
    form = FeedbackForm()
    # Feedback submission logic here
    feedbacks = Feedback.query.all()
    return render_template(
        'feedback_list.html', form=form, feedbacks=feedbacks
    )


if __name__ == '__main__':
    app.run(debug=True)
