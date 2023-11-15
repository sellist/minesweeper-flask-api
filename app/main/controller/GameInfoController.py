import json

from flask import Blueprint

from service import GameService

game_info = Blueprint('game_info', __name__)


@game_info.route('/create', methods=['GET'])
def game_config():
    out = {"width": "", "height": "", "mines": ""}
    return json.dumps(out)


@game_info.route('/game', methods=['GET'])
def game():
    # returns format for Game objects
    config = GameService.create_custom_config(1, 2, 0)
    output = GameService.create_and_start(0, 0, config)
    return output.to_json()
