from src.server import app

def test_root_endpoint_returns_hello_world():
    test_client = app.test_client()
    expected_response = b"hello world"
    actual_response = test_client.get("/")

    assert expected_response == actual_response.data

def test_root_endpoint_returns_200_code():
    test_client = app.test_client()
    actual_response = test_client.get("/")
    
    assert actual_response.status_code == 200

