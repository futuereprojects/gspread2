def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_float(red, green, blue):
    return tuple(x / 255.0 for x in (red, green, blue))


def hex_to_float(hex_code):
    rgb = hex_to_rgb(hex_code)
    return rgb_to_float(*rgb)


class Color:
    def __init__(self, hex_code, alpha=1.0):
        self.hex = hex_code.lstrip('#')
        self.red, self.green, self.blue = hex_to_float(self.hex)
        self.alpha = alpha
