import json
from Classes.moderator import Moderator

class Admin(Moderator):
    def __init__(self, my_moderators):
        Moderator.__init__(self, player_for_control={})
        self.my_moderators = ()

    def admin_as_dict(self):
        admin_as_dict = {
            "type": self.__class__.__name__,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "sessions": self.sessions,
            "wallet": self.wallet,
            "player_for_control": self.player_for_control,
            "my_moderators": self.my_moderators
        }
        return admin_as_dict

    def save(self, file_object_admin):
        json.dump(self.moderator_as_dict(), file_object_admin)

    def load(self, file_object_admin):
        object_as_dict = json.load(file_object_admin)
        self.name = object_as_dict["name"]
        return object_as_dict

    def make_a_moderator(self, my_moderator):
        print("{} is a moderator now".format(my_moderator))