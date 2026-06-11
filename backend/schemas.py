from pydantic import BaseModel

class QuoteResponse(BaseModel):

    id: int

    quote: str

    author: str

    class Config:

        from_attributes = True