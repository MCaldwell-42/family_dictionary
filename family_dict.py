my_family = {
    "sister1": {
        "name": "Annelise",
        "age": 32
    },
    "sister2": {
        "name": "Meredyth",
        "age": 32
    },
    "sister3": {
        "name": "Madelynn",
        "age": 28
    },
    "sister4": {
        "name": "Leandra",
        "age": 22
    },
    "mother": {
        "name": "Patricia",
        "age": 54
    },
    "father": {
        "name": "Ralph",
        "age": 56
    },
    "brother": {
        "name": "Russell",
        "age": 16
    }
}

# family_string = [f"{values['name']} is my {key} and is {values['age']} years old." for key, values in my_family.items()]
# for person in family_string:
#     print(person)


# for fam_member, details in my_family.items():
#     print(f'{details["name"]} is my {fam_member} and is {details["age"]} years old')
    
{ print(f"{value['name']} is my {key} and is {str(value['age'])} years old.") for key,value in my_family.items() }