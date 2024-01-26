import tkinter as tk
from tkinter import font as tkFont
import pyttsx3

class Root(tk.Tk):
    def __init__(self):
        engine = pyttsx3.init()
        super(Root, self).__init__()
        self.title("Morse encoder/decoder")
        self.minsize(1000, 600)
        self.configure(bg='#3f4251')
        buttonsFont = tkFont.Font(family="open sans", size=10, weight='bold')
        titleFont = tkFont.Font(family="open sans", size=30, weight='bold')
        appTitle = tk.Label(self, text="Morse-Text encoder/decoder", foreground="#fffffe", bg = "#3f4251", font = titleFont)
        appTitle.place(x = 180, y = 30)
        appTitle.pack(pady=10)
        # Create a Text widget
        textboxInput = tk.Text(self, width=110, height=8, wrap="word", bg="white", fg="black")
        textboxInput.insert(tk.END, "")
        textboxInput.tag_configure("center", justify="center")
        textboxInput.tag_add("center", "1.0", "end")
        textboxInput.place(x = 50, y = 300)
        modeSelectFont = tkFont.Font(family="Open Sans", size=15, weight='bold')
        modeSelectLabel = tk.Label(self, text="Select mode: ", foreground="#fffffe", bg="#3f4251", font=modeSelectFont)
        modeSelectLabel.place(x=50, y= 150)

        mode = -1
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
            for i in morse_code:
                if i == '.-':
                    text += 'A'
                elif i == '-...':
                    text += 'B'
                elif i == '-.-.':
                    text += 'C'
                elif i == '-..':
                    text += 'D'
                elif i == '.':
                    text += 'E'
                elif i == '..-.':
                    text += 'F'
                elif i == '--.':
                    text += 'G'
                elif i == '....':
                    text += 'H'
                elif i == '..':
                    text += 'I'
                elif i == '.---':
                    text += 'J'
                elif i == '-.-':
                    text += 'K'
                elif i == '.-..':
                    text += 'L'
                elif i == '--':
                    text += 'M'
                elif i == '-.':
                    text += 'N'
                elif i == '---':
                    text += 'O'
                elif i == '.--.':
                    text += 'P'
                elif i == '--.-':
                    text += 'Q'
                elif i == '.-.':
                    text += 'R'
                elif i == '...':
                    text += 'S'
                elif i == '-':
                    text += 'T'
                elif i == '..-':
                    text += 'U'
                elif i == '...-':
                    text += 'V'
                elif i == '.--':
                    text += 'W'
                elif i == '-..-':
                    text += 'X'
                elif i == '-.--':
                    text += 'Y'
                elif i == '--..':
                    text += 'Z'
                elif i == '.----':
                    text += '1'
                elif i == '..---':
                    text += '2'
                elif i == '...--':
                    text += '3'
                elif i == '....-':
                    text += '4'
                elif i == '.....':
                    text += '5'
                elif i == '-....':
                    text += '6'
                elif i == '--...':
                    text += '7'
                elif i == '---..':
                    text += '8'
                elif i == '----.':
                    text += '9'
                elif i == '-----':
                    text += '0'
                elif i == '/':
                    text += ' '

            return text
        modeLabel = tk.Label(self, text="", fg = "#fffffe", bg = "#3f4251", font=modeSelectFont)
        modeLabel.place(x=50, y = 250)
        otherModeLabel = tk.Label(self, text="", fg="#fffffe", bg="#3f4251", font=modeSelectFont)
        otherModeLabel.place(x=50, y=450)
        def toEnglish():
            global mode
            modeLabel.config(text="Morse:")
            otherModeLabel.config(text="Text:")
            mode = 1
        def toMorse():
            global mode
            modeLabel.config(text="Text:")
            otherModeLabel.config(text="Morse:")
            mode = 2

        textboxOutput = tk.Text(self, width=110, height=8, wrap="word", bg="white", fg="black")
        textboxOutput.insert(tk.END, "")
        textboxOutput.tag_configure("center", justify="center")
        textboxOutput.tag_add("center", "1.0", "end")
        textboxOutput.place(x=50, y=500)

        def Translate():
            text_to_translate = textboxInput.get("1.0", tk.END)
            global mode
            if mode == 1:
                textboxOutput.insert("1.0", morse_to_text(text_to_translate))
                engine.say(morse_to_text(text_to_translate))
                engine.runAndWait()
            elif mode == 2:
                textboxOutput.insert("1.0", text_to_morse(text_to_translate))


        butonTranslate = tk.Button(self, text="Translate", font=modeSelectFont, command=Translate, bg="#eebbc3", fg="#232946")
        butonTranslate.pack(pady=10)

        radio_button1 = tk.Radiobutton(self, text="Morse to Text", value="Option 1", font=modeSelectFont, fg="#fffffe", bg="#3f4251", command = toEnglish)
        radio_button2 = tk.Radiobutton(self, text="Text to Morse", value="Option 2", font=modeSelectFont, fg="#fffffe", bg="#3f4251", command = toMorse)
        radio_button1.place(x = 300, y = 150)
        radio_button2.place(x = 500, y = 150)

        textboxOutput = tk.Text(self, width=110, height=8, wrap="word", bg="white", fg="black")
        textboxOutput.insert(tk.END, "")
        textboxOutput.tag_configure("center", justify="center")
        textboxOutput.tag_add("center", "1.0", "end")
        textboxOutput.place(x=50, y=500)

if __name__ == "__main__":
    root = Root()
    root.mainloop()