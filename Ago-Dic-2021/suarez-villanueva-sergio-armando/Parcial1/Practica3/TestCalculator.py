from ClassCalculator import Calculator

Test_Cases = open("Test.txt","r")
Lines = Test_Cases.readlines()
casos = []
res = []
i = 0
while i<len(Lines)-1:
    line = Lines[i].split(' ')
    line[2] = line[2].strip()
    casos.append(line)
    reli = Lines[i+1]
    res.append(reli.strip())
    i += 2

def test_Calculator(case, r):
    X = Calculator(int(case[0]),int(case[2]))
    switch = {
        'mas':X.suma,
        'menos':X.resta,
        'por':X.multi,
        'entre':X.divi,
        'elevado_a':X.pote,
        'raiz_de':X.raiz
        }
    assert switch.get(case[1])() == r
    
for j in range(len(casos)):
    print("Prueba #"+str(j+1))
    if res[j][0] =='E':
        test_Calculator(casos[j],res[j])
    else:
        test_Calculator(casos[j],float(res[j]))