# coding: utf-8
import re
from smart_qq_bot.logger import logger
from smart_qq_bot.signals import on_all_message, on_bot_inited


class HelloWorld:
    def __init__(self, words, command):
        self.words = words
        self.command = command

    def say(self, text):
        if re.match(self.command, text):
            return self.words


@on_bot_inited("HelloBot")
def hello_bot_init(bot):
    logger.info("Plugin Hello Bot is available now!")


@on_all_message(name="HelloBot[say]")
def say_hello(msg, bot):
    hello_word = HelloWorld("Hello World!", re.compile(r"--say hello"))
    result = hello_word.say(msg.content)
    if result:
        bot.reply_msg(msg, result)
