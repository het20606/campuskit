from app import app


def test_home_page_loads():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Study shelf" in response.data


def test_health_endpoint():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_item():
    response = app.test_client().post(
        "/add",
        data={"subject": "Test subject", "title": "Test item", "kind": "Notes"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Test item" in response.data
