import random
import string

class MixEncoder:

    def encode(self, message: str) -> str:
        encoded = ""
        for char in message:
            encoded += char
            encoded += random.choice(string.ascii_letters + string.digits + string.punctuation)
        return encoded

    def decode(self, message: str) -> str:
        return message[::2]
