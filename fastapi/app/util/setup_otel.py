from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.trace import TracerProvider


def setup_otel(app):
    # 设置 TracerProvider
    trace.set_tracer_provider(TracerProvider())

    # 初始化 FastAPI 和 Logging 的自动化追踪
    FastAPIInstrumentor.instrument_app(app)
    LoggingInstrumentor().instrument(set_logging_format=True)
