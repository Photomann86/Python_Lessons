enru_dict = {"AEIOULNSTRАВЕИНОРСТ":1, "DGДКЛМПУ":2, "BCMPБГЕЬЯ":3, "FHVWYЙЫ":4, "KЖЗЦЧ":5, "JXШЭЮ":8, "QZФЩЪ":10}

word = input()
print(sum([i[1] for i in enru_dict.items() for j in word if j.upper() in i[0]]))