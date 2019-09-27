import numpy as np
def crossword(list,word):
	length = len(list)
	str_row = ""
	str_diag = ""
	str_diag1 = ""
	str_col = ""
	word_list = {} 
	for i in range(length):
		str_diag += list[i][i]
		str_diag1 += list[i][length-1-i]
		if str_diag not in word_list:
			word_list[str_diag] = 1
		else:
			word_list[str_diag] += 1
		if str_diag1 not in word_list:
			word_list[str_diag1] = 1
		else:
			word_list[str_diag1] += 1
		for j in range(length):
			str_row += list[i][j]
			if str_row not in word_list:
				word_list[str_row] = 1
			else:
				word_list[str_row] += 1
		str_row = ""
	list_col = np.transpose(list)
	str_diag = ""
	str_diag1 = ""
	length_col = len(list_col)
	for i in range(length_col):
		str_diag += list_col[i][i]
		str_diag1 += list_col[i][length-1-i]
		if str_diag not in word_list:
			word_list[str_diag] = 1
		else:
			word_list[str_diag] += 1
		if str_diag1 not in word_list:
			word_list[str_diag1] = 1
		else:
			word_list[str_diag1] += 1
		for j in range(length_col):
			str_col += list_col[i][j]
			if str_col not in word_list:
				word_list[str_col] = 1
			else:
				word_list[str_col] += 1
		str_col = ""
	print(word_list)
	if word in word_list.keys():
		print("The word " + word + " is found in the dictionary")
	else:
		print("The word " + word + "  is not found in the dictionary")

list = [['s', 'e', 'w'], ['c', 'a', 't'], ['r', 'w', 'y']]
crossword(list,"war")
crossword(list,"raw")
crossword(list,"say")
crossword(list,"eaw")
crossword(list,"cat")
crossword(list,"dog")
