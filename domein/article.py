

class Article():
    def __init__(self, title, text, img):
        self.title = title
        self.text = text
        self.img = img

    def to_string(self):
        return "%s\n\n%s" % (self.title, self.text)