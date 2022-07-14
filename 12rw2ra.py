temp = "Разнообразный и богатый опыт сложившаяся структура, организации напрямую зависит от, позиций занимаемых участниками богатый опыт"
qwerty_2 = {}
for word in temp.split():
    qwerty_2[word] = qwerty_2.setdefault(word, 0) + 1
print(qwerty_2)









