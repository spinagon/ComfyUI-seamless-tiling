class SeamlessTile:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"model": ("MODEL",),
                    "tiling": (["enable", "disable"],),
                    },
                }

    CATEGORY = "conditioning"

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "run"
    def run(self, model, tiling):
        if tiling == "enable":
            modify(model.model, circular=True)
        else:
            modify(model.model, circular=False)
        return (model,)

def modify(m, circular=True):
    for child in m.children():
        if "Conv2d" in str(type(child)):
            if circular:
                child.padding_mode = "circular"
            else:
                child.padding_mode = "zeros"
        modify(child, circular)