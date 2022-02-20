def init_app(app):
    # import blueprint to register
    from .home import home_bp
    app.register_blueprint(home_bp)
