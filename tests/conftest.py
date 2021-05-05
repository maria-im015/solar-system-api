import pytest
from app import create_app
from app import db
from app.models.planet import Planet
#from planet import planet 

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    earth = Planet(id = 1,
                   name="earth",
                   description="only planet with life",
                   order=3)
    
    mars = Planet(id =2,
                 name="mars",
                 description="the red planet",
                 order=4)
    
    db.session.add_all([earth, mars])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()
    
''' @pytest.fixture
def planet_data(app):
    new_planet_instance = Planet(name="venus", description="hot hot hot", order=2)
    db.session.add(new_planet_instance)
    db.session.commit() '''
    
    
    
    
    
    
    ''' return {
    "name": "venus",
    "description": "hot hot hot",
    "order" : 2
    } '''