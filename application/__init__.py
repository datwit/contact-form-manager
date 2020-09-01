from flask import Flask


def create_app(config):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    # Initialize Plugins

    with app.app_context():
        # Include our Routes
        from application.routes import default
        
        # Register Blueprints
        app.register_blueprint(default)

        return app
