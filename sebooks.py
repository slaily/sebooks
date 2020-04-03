from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from app import create_app
from app.routes import main


app = create_app()
app.register_blueprint(main)
# Add prometheus wsgi middleware to route /metrics requests
app_dispatcher = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})
