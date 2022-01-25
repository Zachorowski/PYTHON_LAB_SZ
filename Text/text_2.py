

words_dictionary = {" i ": " oraz ", " oraz ": " i ", " nigdy ": " prawie nigdy ", " dlaczego ": " czemu "}

with open("tekst.txt", 'r') as text_file:
    temp_text = text_file.read()


for word in words_dictionary:
    temp_text = temp_text.replace(word, words_dictionary[word])

with open("replaced_file.txt", 'w') as replaced_file_temp:
    replaced_file_temp.write(temp_text)


text_file.close()
replaced_file_temp.close()
