zadanie = 'В строке удалить все буквы "а" и подсчитать количество удаленных символов.'
s = 'Таня кидала в реку арбуз'
string = ''
for i in range(len(s)):
	if (s[i]!='а' and s[i]!='А'):
		string+=s[i]	
print(s)
print(string)		
print('Количество удаленных символов:', len(s)-len(string))	
