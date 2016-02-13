import json

class Session(object):
    def __init__(self, starttime, finishtime = None):
        self.starttime = starttime
        self.finishtime = finishtime

    def session_as_dict(self):
        session_as_dict = {
            "starttime": self.starttime,
            "finishtime": self.finishtime
        }
        return session_as_dict

    def save(self, file_object):
        json.dump(self.session_as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.starttime = object_as_dict["starttime"]
        self.finishtime = object_as_dict["finishtime"]
        return object_as_dict

    def __str__(self):
        return '(starttime = {}, finishtime = {})'.format(self.starttime, self.finishtime)

    def __repr__(self):
        return '(starttime = {}, finishtime = {})'.format(self.starttime, self.finishtime)