from service import GameService
import settings
settings.load_environment()

if __name__ == '__main__':
    gs = GameService
    con = gs.create_custom_config(4, 4, 2)
    g = gs.create(con)
    print(g.board)
    print(g.config)
    g = gs.move(0, 0, g)
    print(g.board)
    print(g.config)
    g = gs.move(2, 2, g)
    print(g.board)
    print(g.config)
