from model.group import Group

def test_modify_first_group_name(app):
    app.group.modify_first(Group(name="New_group"))

def test_modify_first_group_header(app):
    app.group.modify_first(Group(header="New_header"))

def test_modify_first_group_footer(app):
    app.group.modify_first(Group(footer="New_footer"))