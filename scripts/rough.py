# import json
# import nltk

# with open("data//intents.json", "r") as outfile :
#     intents = json.loads(outfile.read())['intents']

# for intent in intents :
#     for query in intent["patterns"] :
#         patterns = [["which day is it", "what is the date", "date", "which day"],
#                     ["what is the time", "time"],
#                     ["start an application", "run", "execute", "start"],
#                     ]
#         # print(query)
#         for pattern_list in patterns :
#             if any([word in nltk.word_tokenize(w) for word in nltk.word_tokenize(query) for w in pattern_list]) :
#                 print(f"query: {query}       pattern_list: {pattern_list}")

import tkinter as tk
import tkinter.ttk as ttk
import time

class Root(tk.Tk) :
    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.val = ""

    def main(self) :
        self.label = tk.Label(self, text=self.val)
        self.label.pack()
        self.next()

    def next(self) :
        # time.sleep(3)
        self.val = "Hello there this is the text to show!"
        self.label.configure(text=self.val)

root = Root()
root.main()
root.mainloop()