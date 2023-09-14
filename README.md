# ComfyUI-seamless-tiling  
ComfyUI nodes for generating seamless textures.  
Replicates "Tiling" option from A1111.  

Use "Seamless Tile" node between loader and samplers to modify model, and "Circular VAE Decode" node to decode image.  
"Offset Image" node to check for seams.

Circular VAE Decode code from https://github.com/FlyingFireCo/tiled_ksampler
