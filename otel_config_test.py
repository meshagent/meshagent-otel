from opentelemetry.sdk.metrics.view import DropAggregation

from meshagent.otel import _metric_views


def test_metric_views_drop_internal_sdk_span_metrics() -> None:
    views = _metric_views()

    assert tuple(view._instrument_name for view in views) == (
        "otel.sdk.span.live",
        "otel.sdk.span.started",
    )
    assert all(isinstance(view._aggregation, DropAggregation) for view in views)
