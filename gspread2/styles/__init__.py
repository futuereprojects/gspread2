from . import colors, borders, api


__all__ = ['api', 'Font', 'borders', 'colors']


class Font:
    def __init__(self, name=None, size=None, bold=None, italic=None, strikethrough=None, underline=None, color=None):
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline
        if color is None:
            self.color = None
        else:
            self.color = color if isinstance(color, colors.Color) else colors.Color(color)
