import yaml

with open('sample.yaml', 'r') as f:
  
  data = yaml.load(f, Loader=yaml.FullLoader)
  
  #Ids multiplos de 3
  for person in data["person"]:
    if int(person["id"]) % 3 == 0:
      print(person)
  
  #apellido o nombre con 5 letras
  for person in data["person"]:
    if len(person["first_name"]) == 5 or len(person["last_name"]) == 5:
      print("\n", person)
  
  #reemplazar el email con ---
  for person in data["person"]:
    person["email"] = "---"
    print(person)