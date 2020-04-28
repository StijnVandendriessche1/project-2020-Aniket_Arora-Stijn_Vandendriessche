class User():
    def __init__(self, name, nickname, email):
        self.name = name
        self.nickname = nickname
        self.email = email

    def to_string(self):
        return "name: %s\nnickname: %s\nemail: %s" % (self.name, self.nickname, self.email)