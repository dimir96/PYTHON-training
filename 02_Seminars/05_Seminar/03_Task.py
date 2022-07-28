# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв"

text = 'skвывдалып абвsf абвdskf ывладофжы абвsdfsd'

text = text.split()

print(' '.join(word for word in text if 'абв' not in word))

