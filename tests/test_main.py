def test_health_check(client):
    """
    Verifies that the API starts correctly in the test environment 
    and the routing is properly mapped.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "Geospatial API is running."
    }