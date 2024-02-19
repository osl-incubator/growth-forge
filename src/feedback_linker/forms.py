"""Forms module."""
from __future__ import annotations

from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.ext.sqlalchemy.fields import (
    QuerySelectField,
    QuerySelectMultipleField,
)
from wtforms.validators import DataRequired, Email, Length

from .models import Link, Person, Project


def project_choices():
    """Return the choices for project."""
    return Project.query.all()


def person_choices():
    """Return the choices for person."""
    return Person.query.all()


class LoginForm(FlaskForm):
    """The login form."""

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6)]
    )
    submit = SubmitField('Log In')


class ProjectForm(FlaskForm):
    """The project form."""

    name = StringField('Project Name', validators=[DataRequired()])
    people = QuerySelectMultipleField(
        'Select People', query_factory=person_choices, get_label='name'
    )
    submit = SubmitField('Submit')


class PersonForm(FlaskForm):
    """The person form."""

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    projects = QuerySelectMultipleField(
        'Select Projects', query_factory=project_choices, get_label='name'
    )
    submit = SubmitField('Submit')


class LinkForm(FlaskForm):
    """The link form."""

    person_one = QuerySelectField(
        'Person One',
        query_factory=person_choices,
        get_label='name',
        validators=[DataRequired()],
    )
    person_two = QuerySelectField(
        'Person Two',
        query_factory=person_choices,
        get_label='name',
        validators=[DataRequired()],
    )
    supervisor = QuerySelectField(
        'Supervisor',
        query_factory=person_choices,
        get_label='name',
        validators=[DataRequired()],
    )
    periodicity = SelectField(
        'Periodicity',
        choices=[
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
        ],
        validators=[DataRequired()],
    )
    times = IntegerField('Every X times', validators=[DataRequired()])
    submit = SubmitField('Submit')


class FeedbackForm(FlaskForm):
    """The feedback form."""

    content = TextAreaField('Feedback Content', validators=[DataRequired()])
    link = QuerySelectField(
        'Link',
        query_factory=lambda: Link.query.all(),
        get_label='id',
        validators=[DataRequired()],
    )
    submit = SubmitField('Submit')


def init_app(app) -> None:
    """Initialize the app for forms."""
    # This function is here if you need to initialize anything specifically
    # for the forms
    pass
