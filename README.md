SmartQQBot
==========

+ 本程序源自[SmartQQBot](https://github.com/Yinzo/SmartQQBot)，在其基础上添加了自制的插件，并去除了部分原有的插件。仅用作自娱自乐用途。
+ 原README见[README](resources/README.md)，其中包含运行原程序所需的依赖包、启动原程序的方式、原程序的特性及功能等说明。本程序所需的依赖、启动方式等一切与原程序相同。
+ [resources](resources/)文件夹中有[使用文档](resources/UserGuide.md)，[二次开发文档](resources/DevelopersGuide.md)，[贡献文档](resources/ContributionGuide.md)，[API文档](resources/API.md)，[常见问题](resources/FAQ.md)等说明文档。

## 添加的插件
+ [`hello_bot`](src/hello_bot.py)：一开始测试用的插件，无论是在讨论组、群或是私聊中，使用命令`--say hello`，机器人就会返回一句“hello world!”
+ [`rock_paper_scissors`](src/rock_paper_scissors.py)：进行简单石头剪刀布游戏的插件。