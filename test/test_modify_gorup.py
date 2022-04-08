from model.group import Group

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(name="New_group"))

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(header="New_header"))

def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(footer="New_footer"))