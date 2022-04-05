from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    # edit first contact in list
    app.contact.edit_first(Contact(firstname="Petya", lastname="Tapkin", company="Luntik", mobile="+79993332211", email="petya@test.test"))
    app.session.logout()