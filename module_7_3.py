class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_worlds = {}
        punktuathion = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            with (open(file, 'r', encoding='utf-8')) as file_open:
                text = []
                for stroka in file_open:
                    stroka = stroka.lower()
                    for punct in punktuathion:
                        stroka = stroka.replace(punct, '')
                    text += stroka.split(' ')
                all_worlds[file] = text
        return all_worlds

    def find(self, word):
        all_worlds = self.get_all_words()
        word = word.lower()
        rezult = {}
        for name, words in all_worlds.items():
            if word in words:
                rezult[name] = words.index(word) + 1
                return rezult

    def count(self, word):
        all_worlds = self.get_all_words()
        word = word.lower()
        amount, rezult = 0, {}
        for name, words in all_worlds.items():
            if word in words:
                amount = words.count(word)
                rezult[name] = amount
        return rezult


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  #   4 слова teXT в тексте всего