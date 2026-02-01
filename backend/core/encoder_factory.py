from services.mix_encoder import MixEncoder
from services.binary_encoder import BinaryEncoder
from services.understandable_encoder import UnderstandableEncoder
from services.emoji_encoder import EmojiEncoder

class EncoderFactory:

    encoders = {
        "mix": MixEncoder(),
        "binary": BinaryEncoder(),
        "understandable": UnderstandableEncoder(),
        "emoji": EmojiEncoder(),
    }

    @staticmethod
    def get_encoder(encoder_type: str):
        encoder = EncoderFactory.encoders.get(encoder_type.lower())
        if not encoder:
            raise ValueError("Invalid encoding type")
        return encoder
