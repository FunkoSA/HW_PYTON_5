""" 
#b = hex(ord('P'))

list1 = (hex(ord('P'))+hex(ord('Y'))).split('0x')
t = list('C#')
hex_value =[]
result = 0
for i in t:
    result += (int(ord(i)))
print (result)

 """
def summ_codes (number,lang_name):
    '''Функция подсчета суммы очков слова, если его порядковый номер является делитетем'''
    name=list(lang_name)
    scores_summ =0
    for i in name:
        scores_summ += (int(ord(i)))
    if not scores_summ%number:
        return scores_summ  

with open('Python/HW-PY_5/languages.txt','r') as lang_file:
    lang_list = lang_file.read().split('\n')

num_list = [i for i in range(1, len(lang_list)+1)]

lang_list = list(zip(num_list,map(lambda s: s.upper(),lang_list)))
print (f'Вывод списка кортежей (порядковый номер, ЯП)\n{lang_list}\n')

summ_codes_list =[()]
for n in lang_list:
    if (summ_codes(n[0],n[1])):
        summ_codes_list.append((summ_codes(n[0],n[1]),n[1]))
    
del summ_codes_list[0]
print(f'Вывод результата (сумма очков, ЯП)\n{summ_codes_list}\n')





