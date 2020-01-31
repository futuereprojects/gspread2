class Side:
    def __init__(self, border_style=None, color='FF000000', width=1):
        self._border_style = border_style
        self._color = color
        self._width = width

    @property
    def border_style(self):
        return self._border_style.upper()

    @property
    def color(self):
        return self._color

    @property
    def width(self):
        return self._width


class Border:
    def __init__(self, left=None, right=None, top=None, bottom=None):
        # TODO: validate the sides ensuring Side class is used
        self.left, self.right, self.top, self.bottom = left, right, top, bottom
