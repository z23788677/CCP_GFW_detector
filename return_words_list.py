with open("words_list//red_light_word.dat", 'r', encoding="utf-8") as red_light_file:
    red_light_file = red_light_file.read()

with open("words_list//orange_light_word.dat", 'r', encoding="utf-8") as orange_light_word:
    orange_light_file = orange_light_word.read()

with open("words_list//yellow_light_word.dat", 'r', encoding="utf-8") as yellow_light_file:
    yellow_light_file = yellow_light_file.read()

with open("words_list//tradition_red_light_word.dat", 'r', encoding="utf-8") as tr_red_light_file:
    tr_red_light_file = tr_red_light_file.read()

with open("words_list//tradition_orange_light_word.dat", 'r', encoding="utf-8") as tr_orange_light_file:
    tr_orange_light_file = tr_orange_light_file.read()

with open("words_list//tradition_yellow_light_word.dat", 'r', encoding="utf-8") as tr_yellow_light_file:
    tr_yellow_light_file = tr_yellow_light_file.read()

red_list = []
orange_list = []
yellow_list = []
word_container = ""

for word in red_light_file:
    if word != "\n":
        word_container += word
    else:
        red_list.append(word_container)
        word_container = ""

for word in orange_light_file:
    if word != "\n":
        word_container += word
    else:
        orange_list.append(word_container)
        word_container = ""

for word in yellow_light_file:
    if word != "\n":
        word_container += word
    else:
        yellow_list.append(word_container)
        word_container = ""

#TR
for word in tr_red_light_file:
    if word != "\n":
        word_container += word
    else:
        red_list.append(word_container)
        word_container = ""

for word in tr_orange_light_file:
    if word != "\n":
        word_container += word
    else:
        orange_list.append(word_container)
        word_container = ""

for word in tr_yellow_light_file:
    if word != "\n":
        word_container += word
    else:
        yellow_list.append(word_container)
        word_container = ""
orange_list.remove('神韵')
orange_list.remove('神韻')
yellow_list.remove('武汉肺炎')
yellow_list.remove('武漢肺炎')

if __name__ == "__main__":
    print(red_list)