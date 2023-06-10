def polindrom(word):
    return word == word[::-1]

polin = 'шалаш'
res = polindrom(polin)
print(res)


nepolin = 'кот'
res = polindrom(nepolin)
print(res)
