from prometheus_client import Summary


# Create a metric to track time spent and requests made.
request_summary = Summary('request_processing_seconds', 'Time spent processing request')
