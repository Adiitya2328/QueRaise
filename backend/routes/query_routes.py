from fastapi import APIRouter

from backend.models import QueryRequest, QueryResponse
from backend.service import process_question

router = APIRouter()


@router.post(
    "/query",
    response_model=QueryResponse
)
def query_database(
    request: QueryRequest
):

    return process_question(
        request.question
    )