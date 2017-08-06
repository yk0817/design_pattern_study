import abc
import os
import re
import tempfile
import Qtrac
try:
    import cyImage as Image
except ImportError:
    import Image

def main():
    pairs = (("Mon", 16), ("Tue", 17), ("Wed", 19), ("Thu", 22),
            ("Fri", 24), ("Sat", 21), ("Sun", 19))

    textBarCharter = BarCharter(TextBarRenderer())
    textBarCharter.render("Forecast 6/8",pairs)
    imageBarCharter = Barcharter(ImageBarRnderer())
    imageBarCharter.render("Forecast 6/8", pairs)

@Qtrac.has_methods("initialize","draw_caption","draw_bar","finalize")
class BarRenderer(metaclass=abc.ABCMeta): pass

class BarCharter:

    def __init__(self,renderer):
        if not isinstance(renderer,BarRenderer):
            raise TypeError("Expected object of type BarRenderer,got {}".
                            format(type(renderer).__name__))
        self.__renderer = renderer

    def render(self,caption,pairs):
        maximu = max(value for _, value in pairs)
        self.__renderer.initialize(len(pairs),maximum)
        self.__renderer.draw_caption(caption)
        for name,value in pairs:
            self.__renderer.draw_bar(name,value)
        self.__renderer.finalize()

class TextBarRenderer:

    
