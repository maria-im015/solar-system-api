from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
    
def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "earth",
        "description":"only planet with life",
        "order": 3}

def test_get_one_planet_by_name(client, two_saved_planets):
    # Act
    response = client.get("/planets", query_string={"name": "mars"})
    response_body = response.get_json()


    # Assert
    assert response.status_code == 200
    assert response_body == [
        {"id" : 2,
        "name": "mars",
        "description" : "the red planet",
        "order": 4}]
    
    
def test_create_one_planet(client):
    
    new_planet_instance = Planet(name="venus", description="hot hot hot", order=2)
    response = client.post("/planets", json=new_planet_instance.to_json())
    response_body = response.get_data(as_text=True)

    assert response.status_code == 201
    assert response_body == '"Planet venus successfully created"\n' 
