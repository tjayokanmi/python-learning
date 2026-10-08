resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []


def add_resource(item):
    for resource in resources:
        if item["id"] == resource["id"]:
            print(f'Resource ID {resource["id"]} already exists.')
            return
    else:
        resources.append(item)

def list_resources():
    for resource in resources:
        print(
            f'''
            {resource["name"]}  || Total: {resource["total"]} || Available: {resource["available"]}
            '''
        )

def borrow_resource(): 