

def test_delete_first_group(app):
    app.manager.session.login(username="admin", password="secret")
    app.manager.group.delete_first_group()
    app.manager.session.logout()