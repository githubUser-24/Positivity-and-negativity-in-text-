import tkinter as tk
from tkinter import scrolledtext

class SpellCheckerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Spell Checker")

        self.textbox = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.textbox.pack(padx=10, pady=10)

        self.check_button = tk.Button(master, text="Check Spelling", command=self.check_spelling)
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=5)

        # Set up the spell checker
        self.dictionary = ["hello", "world", "python", "spell", "checker", "project", "code"]
        self.spell_checker = SpellChecker()
        self.spell_checker.build_dictionary(self.dictionary)

    def check_spelling(self):
        input_text = self.textbox.get("1.0", tk.END)
        misspelled_words, corrections = self.spell_checker.spell_check(input_text)

        result_text = ""
        if misspelled_words:
            result_text += "Misspelled words: {}\n".format(", ".join(misspelled_words))
            result_text += "Corrections: {}\n".format(corrections)
        else:
            result_text = "No misspelled words found!"

        self.result_label.config(text=result_text)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class SpellChecker:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def build_dictionary(self, words):
        for word in words:
            self.insert_word(word)

    def is_word_in_dictionary(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def suggest_corrections(self, word):
        suggestions = []
        self._dfs_suggestions(self.root, word, "", suggestions)
        return suggestions

    def _dfs_suggestions(self, node, remaining, current, suggestions):
        if node.is_end_of_word:
            suggestions.append(current)

        for char, child_node in node.children.items():
            new_remaining = remaining[1:]
            new_current = current + char
            self._dfs_suggestions(child_node, new_remaining, new_current, suggestions)

    def spell_check(self, text):
        words = text.split()
        misspelled_words = [word for word in words if not self.is_word_in_dictionary(word)]
        corrections = {word: self.suggest_corrections(word) for word in misspelled_words}

        return misspelled_words, corrections

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerGUI(root)
    root.mainloop()

