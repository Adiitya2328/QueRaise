from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    success: bool
    message: str
    sql: str | None
    results: list | None