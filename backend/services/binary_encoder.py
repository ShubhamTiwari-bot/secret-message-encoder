class BinaryEncoder:

    def encode(self, message: str) -> str:
        return " ".join(format(ord(char), "08b") for char in message)

    def decode(self, message: str) -> str:
        chars = message.split()
        return "".join(chr(int(char, 2)) for char in chars)
