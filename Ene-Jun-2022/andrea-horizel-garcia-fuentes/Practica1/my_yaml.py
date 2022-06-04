import yaml

with open('sample.yaml', 'r') as f:
  
  my_yaml = yaml.load(f, Loader=yaml.FullLoader)
  
  for person in my_yaml["person"]:
    if int(person["id"]) % 3 == 0:
      print(person)
  
  for person in my_yaml["person"]:
    if len(person["first_name"]) == 5 or len(person["last_name"]) == 5:
      print("\n", person)
  
  for person in my_yaml["person"]:
    person["email"] = "---"
    print(person)