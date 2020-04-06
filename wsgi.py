from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from app import create_app


app = create_app()
# Add prometheus wsgi middleware to route /metrics requests
app_dispatcher = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})
