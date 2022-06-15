import yaml

with open('sample.yaml', 'r') as f:
  
  my_yaml = yaml.load(f, Loader=yaml.FullLoader)
  
  for Persona in my_yaml["Persona"]:
    if int(Persona["id"]) % 3 == 0:
      print(Persona)
  
  for Persona in my_yaml["Persona"]:
    if len(Persona["Nombre"]) == 5 or len(Persona["Apellido"]) == 5:
      print("\n", Persona)
  
  for Persona in my_yaml["Persona"]:
    Persona["email"] = "---"
    print(Persona)