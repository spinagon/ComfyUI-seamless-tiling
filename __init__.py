from .SeamlessTile import CircularVAEDecode, MakeCircularVAE, OffsetImage, SeamlessTile

NODE_CLASS_MAPPINGS = {
    "SeamlessTile": SeamlessTile,
    "CircularVAEDecode": CircularVAEDecode,
    "MakeCircularVAE": MakeCircularVAE,
    "OffsetImage": OffsetImage,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SeamlessTile": "Seamless Tile",
    "CircularVAEDecode": "Circular VAE Decode (tile)",
    "MakeCircularVAE": "Make Circular VAE",
    "OffsetImage": "Offset Image",
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]
