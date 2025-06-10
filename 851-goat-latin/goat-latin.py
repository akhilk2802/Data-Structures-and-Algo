class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        words = sentence.split()

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i, word in enumerate(words):

            new_word = ""
            if word[0] in vowels:
                new_word = word + 'ma'
            else:
                new_word = word[1:] + word[0] + 'ma'
            
            new_word = new_word + ((i + 1) * 'a')

            words[i] = new_word

        return " ".join(words)