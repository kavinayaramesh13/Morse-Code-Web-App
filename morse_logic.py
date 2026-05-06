morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',
    ' ': '/'
}

reverse_dict = {value: key for key, value in morse_code_dict.items()}

def encode_text(text):
    result = []
    for char in text.upper():
        if char in morse_code_dict:
            result.append(morse_code_dict[char])
    return " ".join(result)

def decode_text(code):
    result = []
    parts = code.split(" ")
    for item in parts:
        if item in reverse_dict:
            result.append(reverse_dict[item])
    return "".join(result)