import arcade
from game import Game
from views import MenuView


def main():
    """ Main function """
    # window = arcade.Window()
    # game = Game(window)
    # window.show_view(MenuView(game))
    # arcade.run()
    p1 = arcade.Vec2(1.0, 1.0)
    p2 = arcade.Vec2(0.0, 1.0)

    if p1 == p2:
        print("p1 equals p2")


if __name__ == "__main__":
    main()
