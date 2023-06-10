def polindrom(word):
    return word == word[::-1]

polin = 'шалаш'
res = polindrom(polin)
print(res)


nepolin = 'котт'
res = polindrom(nepolin)
print(res)
