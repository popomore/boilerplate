import logging
import time
import traceback

from fastapi import Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

logger = logging.getLogger(__name__)

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            body = await request.json()
        except Exception:
            body = "Could not parse JSON"
        logger.info(
            f"{request.url.path} Received request, body={body}"
        )

        start_time = time.perf_counter()
        status = "T"
        try:
            response: Response = await call_next(request)
            return response
        except Exception as e:
            status = "F"
            logging.error(f"{request.url.path} Response exception, error={traceback.format_exc()}")
            return JSONResponse(
                content={"detail": f"An error occurred: {str(e)}"}, status_code=500
            )
        finally:
            duration = time.perf_counter() - start_time
            logger.info(f"{request.url.path} completed duration={duration}, status={status}")
