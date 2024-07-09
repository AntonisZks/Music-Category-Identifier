import numpy as np
from matplotlib.colors import LinearSegmentedColormap


def hex_to_rgb(hex_color: str):
    """ Converts HEX color to RGB tuple. """

    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color: tuple[int, int, int]):
    """ Converts RGB tuple to HEX color. """

    return '#{:02x}{:02x}{:02x}'.format(*rgb_color)

def get_hex_color(hex_color):
    """ Returns just the hex color. """

    return hex_color

def invert_hex_color(hex_color: str):
    """ Inverts a hex color. """

    rgb_color = hex_to_rgb(hex_color)
    inverted_rgb = tuple(255 - c for c in rgb_color)
    return rgb_to_hex(inverted_rgb)

def get_colormap(cmap):
    """ Returns just the cmap. """
    
    return cmap

def invert_colormap(cmap):
    """ Inverts a given colormap. """
    
    colors = cmap(np.arange(cmap.N))
    inverted_colors = 1 - colors[:, :3]  # Invert RGB values, ignore alpha
    inverted_cmap = LinearSegmentedColormap.from_list(f'{cmap.name}_inverted', inverted_colors, cmap.N)
    return inverted_cmap
