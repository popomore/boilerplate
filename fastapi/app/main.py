from fastapi import FastAPI

from app.middleware.error_handler import ErrorHandlerMiddleware
from app.router.user import router as user_router
from app.util.lifespan import lifespan
from app.util.setup_otel import setup_otel

app = FastAPI(
    lifespan=lifespan,
)

# middleware
app.add_middleware(ErrorHandlerMiddleware)

# router
app.include_router(user_router)

# init open telemetry
setup_otel(app)
