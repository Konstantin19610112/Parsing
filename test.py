filename = '1.txt'
file = open(filename)
txt_list = file.readlines()
file.close()

print(txt_list)

newline = ''
l = len(txt_list)

for i in range(l):
    sym = txt_list[i][0] + ' '
    newline += sym

print(newline)

filenew = '1new.txt'
file = open(filenew, 'w')
file.write(newline)
file.close()

