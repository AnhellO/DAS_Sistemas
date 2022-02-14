""" 10-2. Learning C: You can use the replace() method to replace any word
in a string with a different word. Here's a quick example showing how to
replace 'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'  
Read in each line from the file you just created, learning_python.txt, and 
replace the word Python with the name of another language, such as C. Print 
each modified line to the screen. """

filename = "learning_python.txt"
msg = f"\n Reading \"{filename}\", replacing\n the word \"Python\" with \"Java\""

print(msg)
with open(filename) as file_object:
    for line in file_object:
        message = line.replace("Python", "Java")
        print("- " + message.strip())

#  Reading "learning_python.txt", replacing
#  the word "Python" with "Java"
# - In Java you can do Data Analytics
# - In Java you can program an AI algorithm
# - In Java you can create GUI applications
# - In Java you can do Data Visualization
