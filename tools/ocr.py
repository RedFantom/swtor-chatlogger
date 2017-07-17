# -*- coding: utf-8 -*-

# Copyright (C) 2017 by RedFantom
# For license see LICENSE
from threading import Thread
from PIL import ImageGrab
from guiparser import get_chatbox_box
from simpleocr import OCR, enhance_image, pil_to_imagebuffer, open_image, imagebuffer_to_pil
from .utilities import get_assets_directory
import os
from pytesseract import image_to_string


class OCRLoop(Thread):
    def __init__(self, character_name, callback=None, exitq=None):
        Thread.__init__(self)
        self.callback = callback
        self.exit_queue = exitq
        self.flag = True
        self.ocr = OCR(grounder="user")
        self.player_name = character_name

    def run(self):
        while self.flag:
            # Get the chat box position
            image = ImageGrab.grab(get_chatbox_box(self.player_name))
            text = image_to_string(image)
            if callable(self.callback):
                self.callback("general", text)
            continue

    def train(self):
        # image = open_image(os.path.join(get_assets_directory(), "template.png"))
        # image = enhance_image(image, color=0.0, contrast=5.1, sharpness=2.0, invert=False)  # sa, sharpness=10.0)
        # pil = imagebuffer_to_pil(image)
        # pil.show()
        # self.ocr.ground(image)
        # self.ocr.train(image)
        pass

    def close(self):
        self.flag = False

