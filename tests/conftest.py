import pytest
from app import create_app
from app import db


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
    earth = Planet(name="EARTH",
                   description="only planet with life",
                   order=3)
    
    mars = Planet(name="MARS",
                 description="the red planet",
                 order=4)
    
    ''' ocean_book = Book(title="Ocean Book",
                      description="watr 4evr")
    mountain_book = Book(title="Mountain Book",
                         description="i luv 2 climb rocks")
 '''
    db.session.add_all([earth, mars])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()