import arcade
from game import Game
from views import MenuView


def main():
    """ Main function """
    window = arcade.Window()
    game = Game(window)
    window.show_view(MenuView(game))
    arcade.run()


if __name__ == "__main__":
    main()
