class TileModel:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"model": ("MODEL",)},
                }

    CATEGORY = "conditioning"

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "run"
    def run(self, model):
        make_circular(model.model)
        return (model,)

def make_circular(m):
    for child in m.children():
        if "Conv2d" in str(type(child)):
            child.padding_mode = "circular"
        make_circular(child)