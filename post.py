class Post:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def json(self):
        return {
            "title": self.title,
            "content": self.content
        }
