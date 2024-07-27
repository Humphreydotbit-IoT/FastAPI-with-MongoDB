from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

route = APIRouter()

#get method
@route.get("/todos")
async def get_all_todos():
    todos = (collection_name.find())   #find all the data in the collection
    return list_serial(todos)  #to convert the list of mongodb documents to a serializable formate before returning it from the FastAPI endpoint

#post method
@route.post("/todos")
async def create_todos(todo: Todo):
    collection_name.insert_one(dict(todo))



#put method
@route.put("/todos/{todo_id}")
async def update_todo(todo_id: str, todo: Todo):
    collection_name.update_one({"_id": ObjectId(todo_id)}, {"$set": dict(todo)})

#delete method
@route.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    collection_name.delete_one({"_id": ObjectId(todo_id)})