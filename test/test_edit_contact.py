from model.contact import Contact

def test_add_contact(app):
    app.contact.edit_first(Contact(firstname="Petya", lastname="Tapkin", company="Luntik", mobile="+79993332211", email="petya@test.test"))
