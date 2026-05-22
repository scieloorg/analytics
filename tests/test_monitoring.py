import unittest

from analytics import monitoring


class MonitoringTest(unittest.TestCase):
    def test_metrics_response_contains_http_metric(self):
        body, content_type = monitoring.metrics_response()
        self.assertTrue(content_type.startswith("text/plain; version="))
        self.assertIn(b"analytics_http_requests_total", body)
