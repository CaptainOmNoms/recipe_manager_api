from db import db


class IngredientModel(db.Model):
    __tablename__ = 'items'

    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    
    def __init__(self, name):
        self.name = name
        self.price = price
        
    def json(self):
        return {
            'id': self.ingredient_id,
            'name': self.name,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()