from fastapi import APIRouter

from backend.models import (
    QueryRequest,
    QueryResponse,
    DatabaseConnectionRequest
)
from backend.service import process_question
from backend.database import test_connection

router = APIRouter()


@router.post(
    "/query",
    response_model=QueryResponse
)
def query_database(
    request: QueryRequest
):

    return process_question(
        question=request.question,
        host=request.host,
        port=request.port,
        database=request.database,
        user=request.user,
        password=request.password
    )

@router.post("/test-connection")
def test_database_connection(
    request: DatabaseConnectionRequest
):

    connected = test_connection(
        host=request.host,
        port=request.port,
        database=request.database,
        user=request.user,
        password=request.password
    )

    return {
        "success": connected
    }