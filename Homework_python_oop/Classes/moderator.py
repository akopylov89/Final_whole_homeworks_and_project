import json
from Classes.player import Player

class Moderator(Player):
    def __init__(self, player_for_control):
        Player.__init__(self)
        self.player_for_control = {}

    def moderator_as_dict(self):
        moderator_as_dict = {
            "type": self.__class__.__name__,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "sessions": self.sessions,
            "wallet": self.wallet,
            "player_for_control": self.player_for_control
        }
        return moderator_as_dict

    def save(self, file_object_moderator):
        json.dump(self.moderator_as_dict(), file_object_moderator)

    def load(self, file_object_moderator):
        object_as_dict = json.load(file_object_moderator)
        self.name = object_as_dict["name"]
        return object_as_dict

    def give_a_ban(self, player_for_control):
        self.player_for_control[player_for_control] = "banned"
        print("Player {} is banned".format(player_for_control))

    def take_a_ban(self, player_for_control):
        if player_for_control in self.player_for_control.keys():
            self.player_for_control[player_for_control] = "unbanned"
            print("Player {} is unbanned".format(player_for_control))
        else:
            raise Exception('Ban error: {} is not banned'.format(player_for_control))

    def __repr__(self):
        return '{}'.format(self. name)
