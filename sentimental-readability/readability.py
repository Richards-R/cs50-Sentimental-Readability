from cs50 import get_string

sent_count = 0
word_count = 1
lett_count = 0

letters = 'abcdefghijklmnopqrstuvwxyz'

text_input = get_string('Text: ')

for i in range(len(text_input)):
    if text_input[i] == '.' or text_input[i] == '!' or text_input[i] == '?':
        sent_count += 1

    elif text_input[i] == ' ':
        word_count += 1

    for j in range(len(letters)):

        text_input_test_letter = text_input[i].lower()

        if text_input_test_letter == letters[j]:
            lett_count += 1

l = float(lett_count / word_count) * 100
s = float(sent_count / word_count) * 100

index = 0.0588 * l - 0.296 * s - 15.8

if index < 1:
    print('Before Grade 1')

elif index >= 16:
    print('Grade 16+')

else:
    print('Grade ', round(index))
