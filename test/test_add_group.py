# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(name="firefox", header="ff1", footer="ff2"))
    app.session.logout()

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


