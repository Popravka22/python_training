from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    #create contact
    app.contact.create_contact(Contact(firstname="Vasya", lastname="Pupkin", company="Opa", mobile="+79112223344", email="vasya@test.test"))
    app.session.logout()