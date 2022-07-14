digits = ['1', '3', '5', '64', '34', '45', '34']
data = open('file.txt', 'w')
data.writelines(digits)
data.close()
