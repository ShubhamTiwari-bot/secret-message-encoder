import hashlib
import random

class UnderstandableEncoder:

    def __init__(self):
        self.forward_map = {}
        self.reverse_map = {}

    def _generate_word(self, word: str) -> str:
        # Create deterministic seed from word
        seed = int(hashlib.md5(word.encode()).hexdigest(), 16)
        random.seed(seed)

        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"

        length = random.randint(4, 8)
        new_word = ""

        for i in range(length):
            if i % 2 == 0:
                new_word += random.choice(consonants)
            else:
                new_word += random.choice(vowels)

        return new_word

    def encode(self, message: str) -> str:
        words = message.lower().split()
        encoded_words = []

        for word in words:
            if word not in self.forward_map:
                new_word = self._generate_word(word)
                self.forward_map[word] = new_word
                self.reverse_map[new_word] = word

            encoded_words.append(self.forward_map[word])

        return " ".join(encoded_words)

    def decode(self, message: str) -> str:
        words = message.lower().split()
        decoded_words = []

        for word in words:
            if word in self.reverse_map:
                decoded_words.append(self.reverse_map[word])
            else:
                decoded_words.append(word)

        return " ".join(decoded_words)
