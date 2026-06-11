from sqlalchemy.orm import Session
from models import Quote

def save_quote(db: Session, quote: str, author: str):

    new_quote = Quote(
        quote=quote,
        author=author
    )

    db.add(new_quote)

    db.commit()

    db.refresh(new_quote)

    return new_quote


def get_history(db: Session):

    return db.query(Quote).all()