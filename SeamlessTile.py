import copy

import torch


class SeamlessTile:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "tiling": (["enable", "disable"],),
                "copy_model": (["Modify in place", "Make a copy"],),
            },
        }

    CATEGORY = "conditioning"

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "run"

    def run(self, model, copy_model, tiling):
        if copy_model == "Modify in place":
            model_copy = model
        else:
            model_copy = copy.deepcopy(model)
        if tiling == "enable":
            model_copy.model.apply(make_circular)
        else:
            model_copy.model.apply(unmake_circular)
        return (model_copy,)


def make_circular(m):
    if isinstance(m, torch.nn.Conv2d):
        m.padding_mode = "circular"


def unmake_circular(m):
    if isinstance(m, torch.nn.Conv2d):
        m.padding_mode = "zeros"


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
        result = (vae.decode(samples["samples"]),)
        for layer in [
            layer
            for layer in vae.first_stage_model.modules()
            if isinstance(layer, torch.nn.Conv2d)
        ]:
            layer.padding_mode = "zeros"
        return result


class MakeCircularVAE:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "vae": ("VAE",),
                "tiling": (["enable", "disable"],),
                "copy_vae": (["Modify in place", "Make a copy"],),
            }
        }

    RETURN_TYPES = ("VAE",)
    FUNCTION = "run"

    CATEGORY = "latent"

    def run(self, vae, tiling, copy_vae):
        if copy_vae == "Modify in place":
            vae_copy = vae
        else:
            vae_copy = copy.deepcopy(vae)
        if tiling == "enable":
            vae_copy.first_stage_model.apply(make_circular)
        else:
            vae_copy.first_stage_model.apply(unmake_circular)
        return (vae_copy,)
