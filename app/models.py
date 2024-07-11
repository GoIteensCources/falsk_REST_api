from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db


class QuotesModel(db.Model):
    __tablename__ = "quotes"

    id: Mapped[int] = mapped_column(primary_key=True)
    quote: Mapped[str] = mapped_column(sa.String(255))
    author: Mapped[str] = mapped_column(sa.String(50))

    def __str__(self):
        return f"{self.quote}: {self.author}"

    @classmethod
    def get_all(cls) -> list:
        data_quote = db.session.execute(db.select(cls)).scalars()
        return [{'id': quote.id, "author": quote.author, "quote": quote.quote} for quote in data_quote]

    @classmethod
    def get_by_id(cls, id: int):
        data_quote = db.session.execute(db.select(cls).where(cls.id == id)).scalar()
        if data_quote:
            return {'id': data_quote.id,
                    "author": data_quote.author,
                    "quote": data_quote.quote
                    }
        return

    @classmethod
    def create(cls, quote: str, author: str) -> int:
        add_data = cls(quote=quote, author=author)
        db.session.add(add_data)
        db.session.commit()

        quote = db.session.execute(db.select(cls).where(cls.quote == quote)).scalar()
        return quote.id

    @classmethod
    def delete(cls, id):
        data_quote = db.session.execute(db.select(cls).where(cls.id == id)).scalar()
        if data_quote:
            db.session.delete(data_quote)
            db.session.commit()


    @classmethod
    def update(cls, id: int, quote: str = None, author: str = None):
        data_quote = db.session.execute(db.select(cls).where(cls.id == id)).scalar()

        if quote:
            data_quote.quote = quote
        if author:
            data_quote.author = author
        db.session.commit()

