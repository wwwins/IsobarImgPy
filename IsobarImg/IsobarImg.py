# -*- coding: utf-8 -*-
#
# IsobarImg.py
#
# Usage:
#    import IsobarImg
#    o = IsobarImg.overlayImage(bg_fn="bg.jpg", fg_fn="title.png")
#    o.save("test.png")


from PIL import Image

def overlayImage(bg_fn, fg_fn):
    """overlay an transparent image
    
    Arguments:
        bg_fn {str} -- bg image filename
        fg_fn {str} -- fg image filename
    
    Returns:
        [image] -- PIL image object
    """
    bg = Image.open(bg_fn)
    fg = Image.open(fg_fn)
    if bg.mode == 'RGB':
        bg = bg.convert("RGBA")
    if fg.mode == 'RGB':
        fg = fg.convert("RGBA")
    return Image.alpha_composite(bg, fg)
