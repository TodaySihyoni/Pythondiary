# 문제 1

word_list = ['apple','watch','apolo','star','abocado']

word_list2 = [i for i in word_list if i[0] == 's' ]
print(word_list2)

name_list = []


# 문제 2       

drug_list  = ['오메가3', None,'비타민C500',None,'홍삼절편']

drug_list2 = [i if i != None else '' for i in drug_list]
print(drug_list2)