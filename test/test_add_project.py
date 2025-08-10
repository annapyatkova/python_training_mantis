from model.project import Project


def test_add_project(app, db, json_projects):
    app.session.ensure_login(username="administrator", password="root")
    project = json_projects
    old_projects = db.get_project_list()
    old_projects_soap = app.soap.list_projects("administrator", "root")
    app.project.create(project)
    new_projects = db.get_project_list()
    new_projects_soap = app.soap.list_projects("administrator", "root")
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
    assert len(old_projects_soap) + 1 == len(new_projects_soap)