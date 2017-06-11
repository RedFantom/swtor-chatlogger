# -*- coding: utf-8 -*-

# Copyright (C) 2017 by RedFantom
# For license see LICENSE
from threading import Thread
from PIL import ImageGrab


class OCRLoop(Thread):
    def __init__(self, callback=None, exitq=None):
        Thread.__init__(self)
        self.callback = callback
        self.exit_queue = exitq

    def run(self):
        pass

