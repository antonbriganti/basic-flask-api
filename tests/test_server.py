from src.server import app
import json

def test_root_endpoint_returns_hello_world():
    test_client = app.test_client()
    expected_response = b"hello world"
    actual_response = test_client.get("/")

    assert actual_response.data == expected_response

def test_root_endpoint_returns_200_code():
    test_client = app.test_client()
    actual_response = test_client.get("/")
    
    assert actual_response.status_code == 200

def test_health_check_returns_200_when_healthy():
    test_client = app.test_client()
    actual_response = test_client.get("/health")

    assert actual_response.status_code == 200

def test_health_check_returns_healthy_message_when_healthy():
    test_client = app.test_client()

    actual_response = test_client.get("/health")
    response_content = json.loads(actual_response.get_data(as_text=True))

    assert response_content["message"] == "healthy"