import threading
import example
import random
import tkinter as tk


class TypingSpeed():
    def __init__(self):
        self.window= tk.Tk()
        self.window.config(bg='light salmon', pady=30, padx=20)
        self.window.title('Typing Test')
        self.img = tk.PhotoImage(file='images/type.png')
        self.image = tk.Label(image=self.img, bg='light salmon')
        self.image.grid(column=1, row=0)
        self.greeting_one = tk.Label(text='Welcome to the typing test!\nStart typing this phrase in the empty box below.',
                                font=("Courier", 25),
                                fg='white',
                                bg='light salmon', )
        self.greeting_one.grid(column=1, row=1)
        self.example_phrase = None
        self.entry_box = None
        self.phrase_to_type = None
        self.wpm_label = None



    def format_phrase(self):
        self.example_phrase = random.choice(example.paragraphs)
        self.phrase_to_type = tk.Message(self.window, text=self.example_phrase,
                                    font=("Courier", 20),
                                    fg='black',
                                    bg='white',
                                    width=1000)
        self.phrase_to_type.grid(column=1, row=2, pady=15)

    def create_entry_box(self):
        self.entry_box = tk.Entry(self.window, font=("Courier", 15), width=75)
        self.entry_box.grid(column=1, row=3, columnspan=1)



    def get_text(self):
        text = self.entry_box.get()
        typed_words_list = text.split(' ')
        example_words_list = self.example_phrase.split(' ')
        cut_off = len(typed_words_list) + 1
        example_words_same_length = example_words_list[0:cut_off]
        wpm = sum(word in typed_words_list for word in example_words_same_length)
        self.wpm_label = tk.Label(text=f'Your typing speed is {wpm} words per minute.',
                             font=("Courier", 25),
                             fg='white',
                             bg='light salmon', )
        self.wpm_label.grid(column=1, row=4)
        self.start_over = tk.Button(text='Refresh', font=("Courier", 25), command=self.refresh)
        self.start_over.grid(column=1, row=5, pady=20)

    def key_press(self, e):
        self.start_time.start()

    def refresh(self):
        self.phrase_to_type.destroy()
        self.entry_box.destroy()
        self.wpm_label.destroy()
        self.format_phrase()
        self.create_entry_box()
        self.first_letter = self.example_phrase[0]
        self.window.bind(self.first_letter, self.key_press)
        self.start_time = threading.Timer(60, self.get_text)







