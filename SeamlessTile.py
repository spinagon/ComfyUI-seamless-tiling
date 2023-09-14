import torch


class SeamlessTile:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "tiling": (["enable", "disable"],),
            },
        }

    CATEGORY = "conditioning"

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "run"

    def run(self, model, tiling):
        for m in model.model.modules:
            if isinstance(m, torch.nn.Conv2d):
                if tiling == "enable":
                    m.padding_mode = "circular"
                else:
                    m.padding_mode = "zeros"
        return (model,)


class CircularVAEDecode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"samples": ("LATENT",), "vae": ("VAE",)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "decode"

    CATEGORY = "latent"

    def decode(self, vae, samples):
        for layer in [
            layer
            for layer in vae.first_stage_model.modules()
            if isinstance(layer, torch.nn.Conv2d)
        ]:
            layer.padding_mode = "circular"
        return (vae.decode(samples["samples"]),)
