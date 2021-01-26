import datetime

from sqlalchemy import Column, Integer, DateTime, UniqueConstraint

from database import Base


class Rectangle(Base):
    __tablename__ = "Rectangle"

    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    width = Column(Integer)
    height = Column(Integer)
    time = Column(DateTime, default=datetime.datetime.utcnow)

    __table_args__ = (UniqueConstraint('x', 'y', 'width', 'height', name='_unique_rectangle'),)

    @staticmethod
    def _transform(rectangle):
        left = rectangle.x
        right = rectangle.x + rectangle.width
        up = rectangle.y
        down = rectangle.y + rectangle.height
        return left, right, up, down

    def overlap(self, rectangle):
        left_1, right_1, up_1, down_1 = self._transform(self)
        left_2, right_2, up_2, down_2 = self._transform(rectangle)

        if left_1 > right_2 or right_1 < left_2:
            return False
        if up_1 > down_2 or down_1 < up_2:
            return False
        return True

    def __repr__(self):
        return "<Rectangle(x='%s', y='%s', width='%s', height='%s')>" % (
            self.x, self.y, self.width, self.height)
