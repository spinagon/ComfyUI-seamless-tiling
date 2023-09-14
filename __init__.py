from .SeamlessTile import CircularVAEDecode, SeamlessTile

NODE_CLASS_MAPPINGS = {
    "SeamlessTile": SeamlessTile,
    "CircularVAEDecode": CircularVAEDecode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SeamlessTile": "Seamless Tile",
    "CircularVAEDecode": "Circular VAE Decode (tile)",
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]
