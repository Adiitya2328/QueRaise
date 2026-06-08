from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str

    host: str
    port: int
    database: str
    user: str
    password: str


class QueryResponse(BaseModel):
    success: bool
    message: str
    sql: str | None
    results: list | None

class DatabaseConnectionRequest(BaseModel):
    host: str
    port: int
    database: str
    user: str
    password: str