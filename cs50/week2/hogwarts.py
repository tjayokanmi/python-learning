# # students = ["Hermione", "Harry", "Ron", "Draco"]
# # houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# # for d in students:
# #     print(d)



# # for i in range(len(students)):
# #     print(i +1, students[i])

# students = {
#     "Herminone": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(student, students[student], sep = ", ")

students = [
    {"name": "Herminone", "House": "Gryffindor", "Patronus": "Otter"},
    {"name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russell terrier"},
    {"name": "Draco", "House": "Slytherin", "Patronus": None}
]

for student in students: 
    print(student["name"], student["House"], sep = ", ")