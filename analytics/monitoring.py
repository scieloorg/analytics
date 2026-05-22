import time

from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Gauge,
    Histogram,
    generate_latest,
)


HTTP_REQUESTS_TOTAL = Counter(
    "analytics_http_requests_total",
    "Total HTTP requests handled by the app",
    ["method", "route", "status_code"],
)

HTTP_REQUEST_DURATION_SECONDS = Histogram(
    "analytics_http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "route"],
)

HTTP_REQUESTS_IN_PROGRESS = Gauge(
    "analytics_http_requests_in_progress",
    "HTTP requests currently in progress",
    ["method", "route"],
)

BACKEND_CALLS_TOTAL = Counter(
    "analytics_backend_calls_total",
    "Total backend calls by backend and operation",
    ["backend", "operation", "result"],
)

BACKEND_CALL_DURATION_SECONDS = Histogram(
    "analytics_backend_call_duration_seconds",
    "Backend call duration in seconds",
    ["backend", "operation"],
)

BACKEND_INFLIGHT_REJECTED_TOTAL = Counter(
    "analytics_backend_inflight_rejected_total",
    "Rejected backend calls due to inflight guard saturation",
    ["backend", "operation"],
)

CIRCUIT_BREAKER_STATE = Gauge(
    "analytics_circuit_breaker_state",
    "Circuit breaker state (1=open, 0=closed)",
    ["host"],
)

CACHE_BACKEND_INFO = Gauge(
    "analytics_cache_backend_info",
    "Configured cache backend (1 for active backend)",
    ["backend"],
)


def metrics_response():
    return generate_latest(), CONTENT_TYPE_LATEST


def observe_backend_call(backend, operation, callable_obj):
    started_at = time.monotonic()
    try:
        result = callable_obj()
        BACKEND_CALLS_TOTAL.labels(backend=backend, operation=operation, result="success").inc()
        return result
    except Exception:
        BACKEND_CALLS_TOTAL.labels(backend=backend, operation=operation, result="error").inc()
        raise
    finally:
        BACKEND_CALL_DURATION_SECONDS.labels(backend=backend, operation=operation).observe(
            time.monotonic() - started_at
        )
