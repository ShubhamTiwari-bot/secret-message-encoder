class EmojiEncoder:

    def __init__(self):
        # 16 emoji set (hex mapping)
        self.emoji_map = [
            "😀","😁","😂","😃",
            "😄","😅","😆","😉",
            "😊","😋","😎","😍",
            "😘","😗","😙","😚"
        ]

        self.reverse_map = {e: i for i, e in enumerate(self.emoji_map)}

    def encode(self, message: str) -> str:
        # Convert text to hex
        hex_string = message.encode().hex()
        encoded = ""

        for char in hex_string:
            encoded += self.emoji_map[int(char, 16)]

        return encoded

    def decode(self, message: str) -> str:
        hex_string = ""

        for emoji in message:
            if emoji in self.reverse_map:
                hex_string += format(self.reverse_map[emoji], "x")

        return bytes.fromhex(hex_string).decode()
