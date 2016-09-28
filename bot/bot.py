from .basebot import BaseBot
import requests
import time
import re
import json

class Bot(BaseBot):

    def __init__(self, token):
        super().__init__(token)
