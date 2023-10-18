from application import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id              = db.Column(db.Integer, primary_key = True)
    username        = db.Column(db.String(128), nullable = False)
    password        = db.Column(db.String(128), nullable = False)
    fullname        = db.Column(db.String(128), nullable = False)
    profile_pic     = db.Column(db.String(128), deafault = "default.jpg")
    bio             = db.Column(db.String(128), nullable = False)
    join_date       = db.Column(db.DateTime(), default=datetime.utcnow)
    status          = db.Column(db.Boolean(), default = True)
    email           = db.Column(db.String(128))



    #     id            = db.Column(db.Integer, primary_key = True)
    # full_name     = db.Column(db.String(128), nullable = False)
    # email         = db.Column(db.String(128), nullable = False)
    # gender        = db.Column(db.String(128), nullable = False)
    # date_of_birth = db.Column(db.DateTime, nullable = False, default=datetime.utcnow())
    # country_code  = db.Column(db.Integer, nullable = False)
# class Follower(db.Model):
#     __tablename__ = "followers"
#     id = db.Column(db.Integer, primary_key = True)
#     full_name = db.Column(db.String(128), nullable = False)
#     follower = db.Column(db.String, db.ForeignKey("users.id"), nullable = False)
# class Following(db.Model):
#     __tablename__ = "followings"
#     id = db.Column(db.Integer, primary_key = True)
#     full_name = db.Column(db.String(128), nullable = False)
#     following = db.Column(db.String, db.ForeignKey("users.id"), nullable = False)

class Relationship(db.model):
    __tablename__   = 'relationship'
    id              = db.Column(db.Integer, primary_key = True)
    id_follower     = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    id_following    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    status          = db.Column(db.Boolean, default=True)
    relation_date   = db.Column(db.DateTime, default=datetime.utcnow)


class Post(db.Model):
    __tablename__   = "posts"
    id              = db.Column(db.Integer, primary_key = True)
    author_id       = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    img             = db.Column(db.String(128), nullable = False)    
    caption         = db.Column(db.String(128),default="")
    status          = db.Column(db.Boolean, default=True)
    post_date       = db.Column(db.DateTime, nullable = False, default=datetime.utcnow())
    
    

class Comment(db.Model):
    __tablename__   = "comments"
    id              = db.Column(db.Integer, primary_key = True)
    note            = db.Column(db.String(1024), nullable = False)
    commenter_id    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    post_id         = db.Column(db.Integer, db.ForeignKey("post.id"), nullable = False)
    hidden          = db.Column(db.Boolean, default=False)
    commenter_date  = db.Column(db.DateTime, nullable = False, default=datetime.utcnow())
   
class Like(db.Model):
    __tablename__   = "likes"
    id              = db.Column(db.Integer, primary_key = True)
    like_id         = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    post_id         = db.Colum(db.Integer, db.ForeignKey("post.id"), nullable = False)
    status          = db.Column(db.Boolean, default=True)
    like_date       = db.Column(db.DateTime, default=datetime.utcnow)
    