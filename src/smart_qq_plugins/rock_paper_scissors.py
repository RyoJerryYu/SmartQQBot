# coding: utf-8
import re
import random
from smart_qq_bot.logger import logger
from smart_qq_bot.signals import on_all_message, on_bot_inited


class RPS:
    command = (re.compile(r"--rps rock"),
               re.compile(r"--rps paper"),
               re.compile(r"--rps scissor"),
               re.compile("--rps magic(.*?)"))
    words = ("石头", "布", "剪刀")
    status = ("平手啦", "我赢啦", "我输啦")

    def __init__(self, text):
        self.use = 4
        for i in range(0, 4):
            if re.match(RPS.command[i], text):
                self.use = i

    def compare(self, other):
        if other.use == 4:
            return "傻逼网友发的什么鸡巴"
        elif other.use == 3:
            return "是魔法？打不过打不过"
        else:
            com = (self.use - other.use) % 3
            return "我出{0}，你出{1}，{2}".format(
                RPS.words[self.use],
                RPS.words[other.use],
                RPS.status[com])


@on_bot_inited("RockPaperScissors")
def rock_paper_scissors_init(bot):
    logger.info("Plugin rock paper scissors is available now!")


@on_all_message(name="RPS[play]")
def play_rps(msg, bot):
    if re.match("--rps(.*?)", msg.content):
        bot_command = (r"--rps rock", r"--rps paper", r"--rps scissor")
        bot_use = RPS(random.choice(bot_command))
        player_use = RPS(msg.content)
        result = bot_use.compare(player_use)
        if result:
            bot.reply_msg(msg, result)
