# -*- coding: utf-8 -*-

# Copyright (C) 2017 by RedFantom
# For license see LICENSE
from threading import Thread
from PIL import ImageGrab
from guiparser.guiparser import GUIParser
from simpleocr import OCR, enhance_image


class OCRLoop(Thread):
    def __init__(self, callback=None, exitq=None):
        Thread.__init__(self)
        self.callback = callback
        self.exit_queue = exitq
        self.flag = True
        self.ocr = OCR()

    def run(self):
        while self.flag:
            # Get the chat box position
            image = ImageGrab.grab()
            image = enhance_image(image, color=0.0, contrast=2.0, sharpness=2.0)
            text, _, _ = self.ocr.ocr(image)
            if callable(self.callback):
                self.callback(text)
            continue

    def train(self):
        pass

    def close(self):
        self.flag = False

