class EmojiEncoder:

    def __init__(self):

        # Large meaningful emoji dictionary
        self.word_map = {

    # ======================
    # FACIAL EXPRESSIONS
    # ======================
    "happy": "😊",
    "sad": "😢",
    "angry": "😡",
    "excited": "🤩",
    "tired": "😴",
    "confused": "🤔",
    "surprised": "😲",
    "scared": "😱",
    "cool": "😎",
    "love": "😍",
    "cry": "😭",
    "laugh": "😂",
    "serious": "😐",
    "crazy": "🤪",
    "smile": "🙂",
    "wink": "😉",

    # ======================
    # HELPING VERBS
    # ======================
    "is": "🟢",
    "am": "🟢",
    "are": "🟢",
    "was": "🟡",
    "were": "🟡",
    "be": "🔁",
    "will": "🔮",
    "have": "📦",
    "has": "📦",
    "had": "📦",
    "can": "💪",
    "could": "🤲",
    "must": "❗",
    "should": "👍",
    "may": "🌤️",
    "might": "🌩️",

    # ======================
    # GREETINGS
    # ======================
    "hello": "👋",
    "hi": "🙋",
    "welcome": "🎉",
    "thanks": "🙏",
    "sorry": "🙇",
    "morning": "🌅",
    "night": "🌙",
    "goodbye": "👋",
    "bye": "👋",

    # ======================
    # EMOTIONS
    # ======================
    "joy": "😁",
    "fear": "😨",
    "hope": "🌟",
    "peace": "☮️",
    "anger": "🔥",
    "proud": "🏆",
    "strong": "💪",
    "weak": "🥀",

    # ======================
    # NATURE
    # ======================
    "world": "🌍",
    "sun": "☀️",
    "moon": "🌙",
    "star": "⭐",
    "fire": "🔥",
    "water": "💧",
    "tree": "🌳",
    "flower": "🌸",
    "rain": "🌧️",
    "cloud": "☁️",
    "mountain": "🏔️",
    "ocean": "🌊",
    "earth": "🌎",
    "sky": "🌤️",

    # ======================
    # OBJECTS
    # ======================
    "phone": "📱",
    "computer": "💻",
    "car": "🚗",
    "money": "💰",
    "gift": "🎁",
    "book": "📖",
    "food": "🍔",
    "pizza": "🍕",
    "coffee": "☕",
    "house": "🏠",
    "key": "🔑",
    "clock": "⏰",
    "camera": "📷",
    "music": "🎵",

    # ======================
    # ACTIONS
    # ======================
    "run": "🏃",
    "walk": "🚶",
    "sleep": "😴",
    "read": "📚",
    "write": "✍️",
    "code": "👨‍💻",
    "play": "🎮",
    "work": "💼",
    "study": "📖",
    "eat": "🍽️",
    "drink": "🥤",
    "talk": "💬",
    "drive": "🚗",
    "listen": "🎧",

    # ======================
    # ABSTRACT
    # ======================
    "secret": "🤫",
    "message": "💌",
    "idea": "💡",
    "success": "🏆",
    "power": "⚡",
    "freedom": "🕊️",
    "danger": "⚠️",
    "truth": "📜",
    "time": "⏳",
    "future": "🔮",
    "past": "🟡",
    "present": "🟢"
}


        self.reverse_word_map = {v: k for k, v in self.word_map.items()}

        # Large emoji pool for unknown words
        self.pool = [
            "🌟","⚡","🌈","🔥","🌊","🍀","🌙","🌻","💫","🌀",
            "🧩","🎯","🎲","🎨","🛸","🚀","🧠","🔮","🧿","🎧",
            "🌋","🌵","🍎","🍇","🥑","🍩","🍿","🧃","🏝️","🏔️"
        ]

    def encode(self, message: str) -> str:
        words = message.lower().split()
        encoded = []

        for word in words:
            if word in self.word_map:
                encoded.append(self.word_map[word])
            else:
                # Advanced unknown word compression (2 emojis only)
                value = sum(ord(c) for c in word)
                emoji1 = self.pool[value % len(self.pool)]
                emoji2 = self.pool[(value * 7) % len(self.pool)]
                encoded.append(emoji1 + emoji2)

        return " ".join(encoded)

    def decode(self, message: str) -> str:
        parts = message.split()
        decoded = []

        for part in parts:
            if part in self.reverse_word_map:
                decoded.append(self.reverse_word_map[part])
            else:
                decoded.append("[unknown]")

        return " ".join(decoded)
