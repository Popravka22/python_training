from model.contact import Contact
from fixture.application import Application
import time


def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="Vasya", lastname="Pupkin", company="Paparam", mobile="+79112223344",
                                       email="vasya@test.test"))
    time.sleep(5)  # Сон в 5 секунд


def test_add_empty_contact(app):
    app.contact.create_contact(Contact(firstname="", lastname="", company="", mobile="", email=""))
    time.sleep(5)  # Сон в 5 секунд

