from flask import Flask
from src.main.routes.routes import user_route_bp

app = Flask(__name__)
# Registra blueprints
app.register_blueprint(user_route_bp)
