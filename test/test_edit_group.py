from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first(Group(name="test", header="test", footer="test"))
