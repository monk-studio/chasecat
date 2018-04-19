from .base import db
from sqlalchemy import Column
from sqlalchemy import Integer, String


class Leaderboard(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), unique=True, nullable=False)
    user_name = Column(String(20), nullable=False)
    score = Column(Integer, nullable=False)

    def to_dict(self):
        return dict(
            name=self.user_name,
            score=self.score,
        )
