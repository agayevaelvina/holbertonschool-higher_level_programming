from task_03_files import app

def test_products_json():
    with app.test_client() as client:
        response = client.get('/products?source=json')
        assert response.status_code == 200
        assert b'Laptop' in response.data
        assert b'Coffee Mug' in response.data

if __name__ == "__main__":
    test_products_json()
    print("Test passed!")
