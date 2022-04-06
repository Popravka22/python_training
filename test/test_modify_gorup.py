from model.group import Group

def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="New_group"))
    app.session.logout()

def test_modify_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(header="New_header"))
    app.session.logout()

def test_modify_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(footer="New_footer"))
    app.session.logout()