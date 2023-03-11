from flask import Flask
from lesson_02.blog.user.views import user
from lesson_02.blog.report.views import report

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)

