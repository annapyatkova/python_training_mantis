from model.project import Project
import random


def test_delete_some_project(app):
    app.session.ensure_login(username="administrator", password="root")
    # проверить что количество проектов больше 0
    # получить старый список проектов
    # выбрать проект на удаление
    # удалить проект
    app.project.delete_project_by_id(2)
    # получить новый список проектов
    # удалить проект из старого списка
    # проверить что списки равны