with open('SPECS.md', 'r') as f:
            t = f.read()
            print('A:',sum(map(t.count,"aA")),'\nE:',sum(map(t.count,"Ee")),'\nI:',sum(map(t.count,"iI")),'\nO:',sum(map(t.count,"oO")),'\nU:',sum(map(t.count,"uU")))
