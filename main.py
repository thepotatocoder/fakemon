import game
import settings as stg

if __name__ == "__main__":
	game = game.Game((stg.WINDOW_W, stg.WINDOW_H))
	game.loop()