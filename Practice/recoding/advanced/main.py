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

def borrow_resource(fellow_id, resource_id, quantity): 
    if fellow_id in fellows:
        borrower = {
            "fellow_id": fellow_id,
            "resource_id": resource_id,
            "quantity": quantity
            }
        for resource in resources:
            if resource["id"] == resource_id:
                if quantity > 0:
                    if resource["available"] >= quantity:
                        resource["available"] -= quantity
                        borrow_records.append(borrower)
    return

borrow_resource("F001", "R001", 2)

print(resources)
print(borrow_records)