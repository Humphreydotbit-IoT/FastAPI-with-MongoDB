def indivitual_serial (todo) -> dict:
    return {
        "id": str(todo["_id"]),  # _ is a special key in MongoDB of finding a column a key which to return the value
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }

def list_serial(todos) -> list:    #serialize data into dictionary with key and value pair
    return [indivitual_serial(todo) for todo in todos]