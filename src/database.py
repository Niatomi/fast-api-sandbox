from schemas import Post
from uuid import uuid4
from exceptions import PostNotFoundException


class Database():
    
    def __init__(self) -> None:
        self.db = []
        
    def create_post(self, post: Post):
        input_data = post.dict()
        input_data['id'] = uuid4()
        self.db.append(input_data)
        return input_data
    
    def get_all(self):
        return self.db
    
    def get_by_id(self, id: int):
        for el in self.db:
            if el['id'] == id:
                return el
        raise PostNotFoundException()
    
    def update_by_id(self, id: int, post: Post):
        self.delete_by_id(id)
        post = post.dict()
        post['id'] = id
        self.db.append(post)
        return True
        
    def delete_by_id(self, id: int):
        try:
            self.db.pop(id)
            return True
        except IndexError as e:
            raise PostNotFoundException()
        