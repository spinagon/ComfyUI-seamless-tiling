from .SeamlessTile import CircularVAEDecode, MakeCircularVAE, SeamlessTile

NODE_CLASS_MAPPINGS = {
    "SeamlessTile": SeamlessTile,
    "CircularVAEDecode": CircularVAEDecode,
    "MakeCircularVAE": MakeCircularVAE,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SeamlessTile": "Seamless Tile",
    "CircularVAEDecode": "Circular VAE Decode (tile)",
    "MakeCircularVAE": "Make Circular VAE",
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]
