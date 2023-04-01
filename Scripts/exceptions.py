class PostNotFoundException(Exception):
    def __init__(self, name: str = 'Post not found'):
        self.name = name