import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")

    yield fixture

    fixture.session.logout()
    fixture.destroy()


    # def fin():
    #     fixture.session.logout()
    #     fixture.destroy()

    #
    # request.addfinalizer(fin)
    # request.addfinalizer(fixture.destroy)
    # return fixture
