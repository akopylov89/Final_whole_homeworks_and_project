from Classes.admin import Admin
from Classes.moderator import Moderator
from Classes.money import GOLD
from Classes.money import USD
from Classes.player import Player

if __name__ == '__main__':
    name = raw_input("Player name: ")
    player1 = Player(name)
    email = raw_input("Player email: ")
    password = raw_input("Player password: ")
    player1.register(email, password)
    player1.login(password=raw_input("Player password fo login: "))
    player1.init_money()
    player1.give_money(USD, 1000)
    player1.give_money(USD, 2000)
    player1.give_money(GOLD, 20)
    player1.take_money(GOLD, 50)
    player1.logout()


    moder1 = Moderator(name)
    email = raw_input("Moderator email: ")
    password = raw_input("Moderator password: ")
    moder1.register(email, password)
    moder1.login(password=raw_input("Moderator password for login: "))
    moder1.give_a_ban(player_for_control=raw_input("Player for control: "))
    moder1.take_a_ban(player_for_control=raw_input("Player for control: "))
    moder1.logout()



    admin1 = Admin(name)
    email = raw_input("Admin email: ")
    password = raw_input("Admin password: ")
    admin1.register(email, password)
    admin1.login(password=raw_input("Admin password for login: "))
    admin1.make_a_moderator(my_moderator=raw_input("Make a moderator: "))
