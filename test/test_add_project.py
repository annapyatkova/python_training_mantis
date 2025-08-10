from model.project import Project


def test_add_project(app):
    app.session.ensure_login(username="administrator", password="root")
    # передать параметры
    project = Project(name="testProj1",status="stable", description="testDescription")
    # получить старый список проектов
    # создать новый проект
    app.project.create(project)
    # получить новый список проектов из базы
    # к старому списку добавить новый проект
    # сравнить старый и новый списки, отсортированные они должны быть равны