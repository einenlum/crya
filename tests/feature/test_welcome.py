from crya import TestClient


async def test_welcome_page(client: TestClient):
    response = await client.get("/")

    assert response.assert_ok()

    assert "Welcome to crya!" in response.text
    assert "Start customizing your crya application." in response.text
