
# Example.json
Abt_me1 = {"name": "Precious", "fav_food": "Rice and beans", "age": 24, "Country": "Nigeria", "State": "Akwaibom", "is_a_christian": True}

import json
About = json.dumps(Abt_me1, indent=6)
print(About)

with open("OrgFile.txt", "w") as file:
    json.dump(Abt_me1, file)

# Covert from json obj to dict
Abt_me1 = {"name": "Precious", "fav_food": "Rice and beans", "age": 24, "Country": "Nigeria", "State": "Akwaibom", "is_a_christian": True}


About = json.dumps(Abt_me1, indent=6)
print(About)

with open("OrgFile.txt", "r") as file:
    person = json.loads(About)
    print(person)
