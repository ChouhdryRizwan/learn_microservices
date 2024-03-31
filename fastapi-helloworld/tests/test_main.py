from fastapi.testclient import TestClient
from fastapi_helloworld.main import app


def test_root_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_test_desc():
    client = TestClient(app=app)
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Test"}  
    

def test_test_check():
    client = TestClient(app=app)
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Ceck Test"} 
      