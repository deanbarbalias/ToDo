from app import db 
from datetime import datetime 

class PostForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    category = db.Column(db.String(3))
    task = db.Column(db.Text)
    create_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    finish_stamp = db.Column(db.DateTime)
    abondoned = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"PostForm('{self.title}', '{self.category}', '{self.create_stamp}', '{self.finish_stamp}')"

