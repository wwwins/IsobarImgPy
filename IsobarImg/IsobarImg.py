# -*- coding: utf-8 -*-
#
# IsobarImg.py
#
# Usage:
#    import IsobarImg
#    o = IsobarImg.overlayImage(bg_fn="bg.jpg", fg_fn="title.png")
#    o.save("test.png")

import cv2
from PIL import Image

def overlayImage(bg_fn, fg_fn):
    """overlay an transparent image
    
    Arguments:
        bg_fn {str} -- bg image filename
        fg_fn {str} -- fg image filename
    
    Returns:
        image -- PIL image object
    """
    bg = Image.open(bg_fn)
    fg = Image.open(fg_fn)
    if bg.mode == 'RGB':
        bg = bg.convert("RGBA")
    if fg.mode == 'RGB':
        fg = fg.convert("RGBA")
    return Image.alpha_composite(bg, fg)

def denoiseImage(img_fn, d=5, sigma_color=30, sigma_space=30):
    """denoise an image
    
    Arguments:
        img_fn {image} -- PIL image object
    
    Keyword Arguments:
        d {int} -- diameter of each pixel neighborhood (default: {5}) 5,9
        sigma_color {int} -- sigma in color space (default: {30}) 30,50,75
        sigma_space {int} -- sigma in coordinate space (default: {30}) 30,50,75
    
    Returns:
        image -- PIL image object
    """
    img = cv2.imread(img_fn)
    out = cv2.bilateralFilter(img, d, sigma_color, sigma_space)
    return Image.fromarray(out[:,:,(2,1,0)])
