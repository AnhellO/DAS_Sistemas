
a = input()
print()

inputs = [input() for i in range(29)]

print()

entrada = [input() for i in range(2)]

ash = inputs.count('Ash')
aspen = inputs.count('Aspen')
basswood  = inputs.count('Basswood')
beech = inputs.count('Beech')
blackwalnut = inputs.count('Black Walnut')
cherry = inputs.count('Cherry')
cottowood = inputs.count('Cottonwood')
cypress = inputs.count('Cypress')
gum = inputs.count('Gum')
hackerry = inputs.count('Hackberry')
hardmaple = inputs.count('Hard Maple')
hickory = inputs.count('Hickory')
pecan = inputs.count('Pecan')
poplan = inputs.count('Poplan')
redalder = inputs.count('Red Alder')
redelm = inputs.count('Red Elm')
redoak = inputs.count('Red Oak')
sassafras = inputs.count('Sassafras')
softmaple = inputs.count('Soft Maple')
sycamore = inputs.count('Sycamore')
whiteoak = inputs.count('White Oak')
willow = inputs.count('Willow')
yellowirch = inputs.count('Yellow Birch')

ash1 = entrada.count('Ash')
redalder1 = entrada.count('Red Alder')

Promash = (ash/len(inputs))*100
Promaspen = (aspen/len(inputs))*100
Prombasswood = (basswood/len(inputs))*100
Prombeech = (beech/len(inputs))*100
Promblackwalnut = (blackwalnut/len(inputs))*100
Promcherry = (cherry/len(inputs))*100
Promcottonwood  = (cottowood /len(inputs))*100
Promcypress = (cypress/len(inputs))*100
Promgum = (gum/len(inputs))*100
Promhackberry = (hackerry/len(inputs))*100
Promhardmaple = (hardmaple/len(inputs))*100
Promhickory = (hickory/len(inputs))*100
Prompecan = (pecan/len(inputs))*100
Prompoplan = (poplan/len(inputs))*100
Promredalder = (redalder/len(inputs))*100
Promredelm = (redelm/len(inputs))*100
Promredoak = (redoak/len(inputs))*100
Promsassafras = (sassafras/len(inputs))*100
Promsoftmaple = (softmaple/len(inputs))*100
Promsycamore = (sycamore/len(inputs))*100
Promwhiteoak = (whiteoak/len(inputs))*100
Promwillow = (willow/len(inputs))*100
Promyellowbirch = (yellowirch/len(inputs))*100

Promash2 = (ash1/len(entrada))*100
Promredalder2 = (redalder1/len(entrada))*100


D = {'Red Alder': Promredalder, 'Ash': Promash, 'Aspen': Promaspen, 'Basswood': Prombasswood, 'Beech': Prombeech, 'Black Walnut': Promblackwalnut, 'Cherry': Promcherry, 'Cottonwood': Promcottonwood, 'Cypress': Promcypress, 'Gum': Promgum, 'Hackberry': Promhackberry, 'Hard Maple': Promhardmaple, 'Hickory': Promhickory, 'Pecan': Prompecan, 'Poplan': Prompoplan, 'Red Elm': Promredelm, 'Red Oak': Promredoak, 'Sassafras': Promsassafras, 'Soft Maple': Promsoftmaple, 'Sycamore': Promsycamore, 'White Oak': Promwhiteoak, 'Willow': Promwillow, 'Yellow Birch': Promyellowbirch}

Do = {'Ash': Promash2, 'Red Alder': Promredalder2}

especie  = D.keys()
elementos = sorted(D.items())
porcentaje = D.values()

especie2  = Do.keys()
elementos2 = sorted(Do.items())
porcentaje2 = Do.values()

for especie, porcentaje in elementos:
    print(especie, '' ,'{0:.4f}'.format(porcentaje))

print()

for especie2, porcentaje2 in elementos2:
    print(especie2, '' ,'{0:.4f}'.format(porcentaje2))









