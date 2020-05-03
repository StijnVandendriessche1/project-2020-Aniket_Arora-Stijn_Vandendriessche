

class Article():
    def __init__(self, title, text, img, author, likes, shares, comments):
        self.title = title
        self.text = text
        self.img = img
        self.author = author
        self.likes = likes
        self.shares = shares
        self.comments = comments

    def to_string(self):
        return "%s\n\n%s" % (self.title, self.text)