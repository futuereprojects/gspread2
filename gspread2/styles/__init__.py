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
        self.color = colors.Color(color) if color is not None else None
