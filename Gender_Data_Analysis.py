people = [
    {"name": "Ali", "age": 20, "gender": "Male"},
    {"name": "Sara", "age": 21, "gender": "Female"},
    {"name": "Hassan", "age": 22, "gender": "Male"},
    {"name": "Eman", "age": 20, "gender": "Female"},
    {"name": "Ahmed", "age": 23, "gender": "Male"},
    {"name": "Ayesha", "age": 21, "gender": "Female"},
    {"name": "Usman", "age": 24, "gender": "Male"},
    {"name": "Hira", "age": 22, "gender": "Female"},
    {"name": "Hamza", "age": 20, "gender": "Male"},
    {"name": "Laiba", "age": 23, "gender": "Female"}
]

male_count = 0
female_count = 0
male_age_total = 0
female_age_total = 0
total_age = 0

oldest = people[0]
youngest = people[0]

print("------------------ Female Data ------------------")

for person in people:
    if person["gender"] == "Female":
        female_count += 1
        female_age_total += person["age"]
        print("Name:", person["name"], "| Age:", person["age"], "| Gender:", person["gender"])

print("\n------------------ Male Data ------------------")

for person in people:
    if person["gender"] == "Male":
        male_count += 1
        male_age_total += person["age"]
        print("Name:", person["name"], "| Age:", person["age"], "| Gender:", person["gender"])

for person in people:
    total_age += person["age"]

    if person["age"] > oldest["age"]:
        oldest = person

    if person["age"] < youngest["age"]:
        youngest = person

average_age = total_age / len(people)
male_average_age = male_age_total / male_count
female_average_age = female_age_total / female_count

print("\n------------------ Age Analysis ------------------")
print("Oldest Person:", oldest["name"], "| Age:", oldest["age"], "| Gender:", oldest["gender"])
print("Youngest Person:", youngest["name"], "| Age:", youngest["age"], "| Gender:", youngest["gender"])
print("Average Age:", average_age)
print("Male Average Age:", male_average_age)
print("Female Average Age:", female_average_age)

print("\n------------------ Summary ------------------")
print("Total People:", len(people))
print("Male Count:", male_count)
print("Female Count:", female_count)