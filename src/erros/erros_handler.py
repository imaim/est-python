from src.presentation.http_types.http_response import HttpResponse
from src.erros.types import HttpBadRequestError, HttpNotFoundError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError)):
        return HttpResponse(
            status_code = error.status_code,
            body={
                "erros": {
                    "title": error.name,
                    "detail": error.message
                }
            }
        )
    return HttpResponse(
                status_code = 500,
                body={
                    "erros": {
                        "title": "Server Error",
                        "detail": str(error)
                    }
                }
            )
    