fw = open('last.txt' , 'w')
fw.write('what is up? \nlets play!')
fw.close()

fr = open ('last.txt' , 'r')
text = fr.read()
print(text)

fw = open('last.txt' , 'w')
fw.write(text)
fw.close