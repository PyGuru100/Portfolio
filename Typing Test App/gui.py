import tkinter as tk
from english_words import english_words_set
import random
from time import time


master_list = [word for word in english_words_set]


def generate_list():
    words_list = []
    while len(words_list) < 350:
        new_word = random.choice(master_list)
        if new_word not in words_list and len(new_word) <= 7:
            words_list.append(new_word)
    return words_list


window = tk.Tk()
window.title('Typist Be Ye?')
window.geometry('500x600')
window.option_add('*Font', 200)

counter = 0
correct_words = 0
list_of_words = generate_list()

display_words = tk.Label(window, text=list_of_words[counter: counter+5])
entry = tk.Entry(window)
entry.pack()


# I need a useless input variable because Tkinter for some reason feeds something into
# the gosh-darn function when I use the bind function.
# noinspection PyUnusedLocal
def update(useless=None):
    global counter, correct_words, list_of_words, remaining
    if remaining <= 0:
        return
    user_input = entry.get()
    if list_of_words[counter] == user_input.split()[-1]:
        correct_words += 1
    counter += 1
    display_words['text'] = list_of_words[counter: counter+5]
    entry.delete(0, tk.END)
    counter_label['text'] = f'Word count: {counter}'
    percentage_label['text'] = f'Accuracy: {round(100 * correct_words/counter, 2)}%'


entry.bind(sequence='<space>', func=update)
display_words.pack()

timer_label = tk.Label(window, text='Remaining Time: ')
seconds = tk.Label(window, text='00:60')
start = time()
remaining = 60


def update_time():
    global remaining
    remaining = round(60 - (time() - start))
    if remaining <= 0:
        remaining_str = '00'

    elif remaining < 10:
        remaining_str = f"0{remaining}"
    else:
        remaining_str = f"{remaining}"
    seconds['text'] = f"00:{remaining_str}"
    window.after(1000, update_time)


def restart():
    global start, remaining, counter, correct_words, list_of_words
    start, remaining, counter, correct_words = time(), 60, 0, 0
    seconds['text'] = '00:60'
    counter_label['text'] = 'Word count: 0'
    percentage_label['text'] = 'Accuracy: 0%'
    entry.delete(0, tk.END)
    list_of_words = generate_list()
    display_words['text'] = list_of_words[counter: counter+5]


timer_label.pack()
seconds.pack()

counter_label = tk.Label(window, text='Word count: 0')
percentage_label = tk.Label(window, text='Accuracy: 0%')
counter_label.pack()
percentage_label.pack()
restart_button = tk.Button(window, command=restart, text='restart')
restart_button.pack()

window.after(1000, update_time)
window.mainloop()
