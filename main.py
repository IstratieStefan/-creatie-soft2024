import pyttsx3

engine = pyttsx3.init()

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': '/'}


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '
    return morse_code


def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
    return text


def main():
    choice = input("Choose an option (1 for text to Morse code, 2 for Morse code to text): ")

    if choice == '1':
        text_input = input("Enter the text: ")
        morse_output = text_to_morse(text_input)
        print("Morse Code: ", morse_output)

    elif choice == '2':
        morse_input = input("Enter the Morse code (use space to separate codes): ")
        text_output = morse_to_text(morse_input)
        engine.say(text_output)
        engine.runAndWait()
        print("Text: ", text_output)

    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
