from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String) 
    order = db.Column(db.Integer)
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "order":self.order
        }
    
    def to_string(self):
        return f"{self.id}: {self.name} Description: {self.description} Order from the star {self.order} "