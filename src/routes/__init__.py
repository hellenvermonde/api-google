from flask import Blueprint # type: ignore

def register_blueprints(app):
    from src.routes.documents_routes import documents_bp
    from src.routes.tests_routes import testes_bp

    app.register_blueprint(documents_bp, url_prefix='/documents')
    app.register_blueprint(testes_bp, url_prefix='/testes')