from flask import Blueprint, request

from model.dto.BeginRequest import BeginRequest
from service import GameService

game = Blueprint('game', __name__)


@game.route('/start', methods=['POST'])
def start():
    r = request.json
    gs = GameService
    try:
        g = BeginRequest(r)
        return gs.create_from_request(g).to_json()
    except AttributeError:
        return "gug"


@game.route('/move', methods=['POST'])
def move():
    return "move"
