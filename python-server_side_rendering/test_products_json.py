from task_03_files import app

def test_products_json():
    with app.test_client() as client:
        response = client.get('/products?source=json')
        assert response.status_code == 200
        assert b"Laptop" in response.data
        assert b"Coffee Mug" in response.data

def test_invalid_source():
    with app.test_client() as client:
        response = client.get('/products?source=xml')
        assert b"Wrong source" in response.data

def test_invalid_id():
    with app.test_client() as client:
        response = client.get('/products?source=json&id=99')
        assert b"Product not found" in response.data

def test_specific_id():
    with app.test_client() as client:
        response = client.get('/products?source=json&id=1')
        assert b"Laptop" in response.data
        assert b"Coffee Mug" not in response.data

if __name__ == "__main__":
    test_products_json()
    test_invalid_source()
    test_invalid_id()
    test_specific_id()
    print("✅ All tests passed!")
