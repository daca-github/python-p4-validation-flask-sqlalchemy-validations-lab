from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
   
    @validates('name')
    def validates_name(self,key,value):
        if value =="":
            raise ValueError('Name cannot be blank')
        return value
    
    @validates('phone_number')
    def validate_phone_number(self,key,phone_number):
        if len(phone_number) != 10:
            raise ValueError('Phone number must have 10 digits.')
        else:
            return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self,key,content):
        if len(content) < 250:
            raise ValueError('Content must be longer than 250 characters')
        else:
            return content
    
    @validates('summary')
    def validate_summary(self,key,summary):
        if len(summary) >= 250:
            raise ValueError('Summary must be longer than 250 characters')
        else:
            return summary
        
    @validates('category')
    def validates_category(self, key, category):
        categories = ['Fiction', 'Non-Fiction']
        if category not in categories:
            raise ValueError('Category must either be Fiction or Non-Fiction.')
        else:
            return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
    
    @validates('title')
    def validates_click_bait(self, key, value):
        clickbait_keywords = ["Yes", "No"]
        if value not in clickbait_keywords:
            raise ValueError('Clickbait value must be one of the keywords')
        return value
