# Decoding dictionary
decode = {'0':'-', '1':'.'}
# Standard morse code translation
morse_code = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    " --.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"
}

# Assuming input is string
example_input = "1111 1 1011 1011 000  100 000 101 1011 011"
print("Example input:", example_input)

# Convert from Eserom to morse code
dot_dash_input = ''
for val in example_input:
    if val == ' ':
        dot_dash_input += ' '
    else:
        dot_dash_input += decode.get(val)

# Convert from morse to letters
split_morse = dot_dash_input.split(' ')
word_list = []
for val in split_morse:
    if val == '':
        word_list.append(' ')
    else:
        word_list.append(morse_code.get(val))

output_word = ''.join(word_list)
print("Output:",output_word)

