from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts: list[Post] = []

    def __repr__(self):
        return "{} by {} ({} post{})".format(
            self.title,
            self.author,
            len(self.posts),
            "" if len(self.posts) == 1 else "s")

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts]
        }
