from Game import Game
from Mainmenu import MainMenu
from Gameplay import GamePlay

game = Game("Space Invaders", 800, 800)
main_menu = MainMenu(game.screen)
game_play = GamePlay(game.screen)
main_menu.gameplay_scene = game_play
game_play.main_menu = main_menu  # Gán thuộc tính này để chuyển lại

game.run(main_menu)