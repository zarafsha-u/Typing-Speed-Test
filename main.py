import threading
from TypingSpeed import TypingSpeed

new_game = TypingSpeed()


new_game.format_phrase()
new_game.create_entry_box()


def key_press(e):
    start_time.start()


first_letter = new_game.example_phrase[0]
new_game.window.bind(first_letter, key_press)
start_time = threading.Timer(60, new_game.get_text)
new_game.window.mainloop()
