"""Models module."""
from __future__ import annotations

from typing import TYPE_CHECKING

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model

    BaseModel = db.make_declarative_base(Model)
else:
    BaseModel = db.Model


class Project(BaseModel):  # type: ignore[name-defined]
    """Project model."""

    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    people = db.relationship(
        'Person', secondary='project_person', back_populates='projects'
    )
    supervisors = db.relationship('Person', secondary='project_supervisor')


class Person(BaseModel):  # type: ignore[name-defined]
    """Person model."""

    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    projects = db.relationship(
        'Project', secondary='project_person', back_populates='people'
    )
    links = db.relationship(
        'Link', secondary='person_link', back_populates='people'
    )


project_person = db.Table(
    'project_person',
    db.Column(
        'person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True
    ),
    db.Column(
        'project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True
    ),
)

project_supervisor = db.Table(
    'project_supervisor',
    db.Column(
        'person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True
    ),
    db.Column(
        'project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True
    ),
)


class Link(BaseModel):  # type: ignore[name-defined]
    """Link model."""

    __tablename__ = 'link'
    id = db.Column(db.Integer, primary_key=True)
    person_one_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person_two_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    supervisor_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    periodicity = db.Column(db.String(50))
    times = db.Column(db.Integer)
    feedback = db.relationship('Feedback', backref='link', lazy=True)


person_link = db.Table(
    'person_link',
    db.Column(
        'link_id', db.Integer, db.ForeignKey('link.id'), primary_key=True
    ),
    db.Column(
        'person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True
    ),
)


class Feedback(BaseModel):  # type: ignore[name-defined]
    """Feedback model."""

    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    link_id = db.Column(db.Integer, db.ForeignKey('link.id'))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())


def init_app(app) -> None:
    """Initialize app for the database."""
    db.init_app(app)
