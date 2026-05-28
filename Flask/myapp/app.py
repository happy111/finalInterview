from flask import Flask
from config import Config
from db.database import init_db, db
from routes.user_routes import user_bp
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    # Initialize Migrate
    Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(user_bp, url_prefix="/api")

    @app.route("/")
    def home():
        return "Flask Production Structure Ready!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
