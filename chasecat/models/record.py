from .base import db
from sqlalchemy import Column
from sqlalchemy import Integer, String


class Record(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), unique=True, nullable=False)
    user_name = Column(String(20), nullable=False)
    score = Column(Integer, nullable=False)

    @property
    def rank(self):
        ahead = Record.query.filter(Record.score > self.score) \
            .count()
        return ahead + 1

    def to_dict(self):
        return dict(
            name=self.user_name,
            score=self.score,
        )
