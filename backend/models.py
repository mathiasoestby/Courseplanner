from app import db,ma
from datetime import datetime


class Articles(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  body = db.Column(db.Text, nullable=False)
  date = db.Column(db.DateTime, default=datetime.utcnow)


  def __repr__(self):
    return "<Articles %r>" % self.title


class ArticlesShema(ma.Schema):
  class Meta:
    fields = ("id", "title", "body", "date")




article_schema = ArticlesShema()
articles_schema = ArticlesShema(many=True)
