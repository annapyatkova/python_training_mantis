from model.project import Project
import random


def test_delete_some_project(app, db):
    app.session.ensure_login(username="administrator", password="root")
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name="test_project_for_del"))
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    new_project = db.get_project_list()
    assert len(old_project) - 1 == len(new_project)
    old_project.remove(project)
    assert old_project == new_project