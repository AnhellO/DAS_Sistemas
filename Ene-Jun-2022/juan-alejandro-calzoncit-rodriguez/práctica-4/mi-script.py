from black import NewLine
from faker import Faker

def replaceName(newLine):
    newLine = newLine.replace('python', fake.first_name())
    newLine = newLine.replace('Python', fake.first_name())
    return newLine

def openFile(fileName):
    try: 
        with open(file_name) as file_obj:
         lines = file_obj.readlines()
    except FileNotFoundError:
        print('File not found !!!.')         
    else:
        return lines        

def createNewLines(lines):
    newLines = []
    for line in lines:
        newLine = line   
        if 'python' in newLine.lower():        
            print(newLine)
            newLine = replaceName(newLine)        
            print(newLine)                
    
        newLines.append(newLine)
    return newLines


def writeNewFile(file_name, newLines):
    with open(file_name, 'w') as file_obj:
        file_obj.writelines(newLines)

if __name__ == '__main__':

    fake = Faker()

    file_name = 'README.md'
    lines = openFile(file_name)

    newLines = createNewLines(lines)
    file_name = 'README-ALTERADO.md'

    writeNewFile(file_name, newLines)