from quart import Quart
from quart_cors import cors
from app.routes.chat import chat
from dotenv import load_dotenv

load_dotenv()  # This loads the variables from .env

def create_app():
    app = Quart(__name__)
    app = cors(app, allow_origin="*")  # Adjust the origins as per your requirement
    app.register_blueprint(chat)
    return app
