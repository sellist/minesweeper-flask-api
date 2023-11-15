import json
from flask import Blueprint

game_info = Blueprint('game_info', __name__)


@game_info.route('/create', methods=['GET'])
def game_config():
    out = {"width": "", "height": "", "mines": ""}
    return json.dumps(out)
