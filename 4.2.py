class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print("Alphabet:", self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self, lang='En'):
        super().__init__(lang, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "This is an example text in English."
english_alphabet = EngAlphabet()
print("Language:", english_alphabet.lang)
english_alphabet.print()
print("Number of letters:", english_alphabet.letters_num())
print("Is 'A' an English letter?", english_alphabet.is_en_letter('A'))
print("Is 'П' an English letter?", english_alphabet.is_en_letter('П'))
print(EngAlphabet.example())