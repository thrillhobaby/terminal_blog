from database import Database
from models.post import Post

Database.initialize()


print(Database.DATABASE["posts"].find({"blog_id": "123"}))
