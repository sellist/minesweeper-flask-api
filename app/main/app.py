from dependency_injector.containers import Container
from flask import Flask

import settings
from controller.GameController import game
from controller.GameInfoController import game_info


def create_app() -> Flask:
    container = Container()
    app = Flask(__name__)

    app.register_blueprint(game, url_prefix='/game')
    app.register_blueprint(game_info, url_prefix='/game-info')
    app.container = container
    return app


if __name__ == '__main__':
    settings.load_environment()
    create_app().run(debug=True)
