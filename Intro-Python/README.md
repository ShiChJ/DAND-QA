# Python入门项目常见问题解答

## 1. 课程练习代码报错怎么办？

请按照如下三个步骤进行：

1. 查看答案。课程中有部分练习可以直接看到答案，对照和正确答案的不同即可；还有一部分必须回答正确才能看到参考答案，这些练习的答案已统一整理至本页面“Python入门习题答案.py”中；
2. 如果看答案以后，还是希望知道自己的代码有什么错误，或者希望弄明白答案代码的逻辑，请利用[此网站](http://www.pythontutor.com/visualize.html#mode=edit)，可视化代码执行语句，可以看到代码中定义的变量信息，进行DEBUG；（需要注意的是，如果你定义了一个函数，想要排查函数的错误，则必须写一行代码**运行函数**才能进行可视化）；
3. 在经过以上步骤，仍然不知道代码（包括做项目时和项目有关的代码）的出错原因或者某段答案代码的逻辑，请在通关群提供以下信息并@助教，并描述问题。
    - 练习对应的课程章节；
    - 练习界面的截图（如果代码报错，请务必将报错信息全部截图）；
    - 文本格式的代码（从练习界面复制，粘贴到聊天框发送）。
    - **注意**：如果希望解决**自己写的代码中的疑问**，在提供以上信息的同时，最好能说明自己解决问题思路和疑惑的地方，以便助教更好定位你的知识盲点并提供相应建议。仅仅问一句“为什么我的代码不对”并不是推荐的提问方式，因为**重要的不是正确与否，而是实现思路**。直接指出错误并告诉正确答案当然很容易，但对于学员而言，以后实际工作中如果遇到类似问题，没有正确的思路还是无法解决，这点敬请理解。

## 2. 如何运行一个后缀名为.py的文件

请参考本页面的视频“如何运行一个Python文件.mp4”。请注意，和课程不同，视频使用的是“python”命令而不是“python3”命令，但实际上没有区别，使用python即可。

## 3. 在命令行使用“python”命令，提示“python”不是内部或外部命令，也不是可运行的程序或批处理文件。

如果你未下载Python，请根据课程提示下载。如果你已下载Python，请参考此[中文链接](http://www.runoob.com/python/python-install.html)中“环境变量配置”部分，配置环境变量。如果英文阅读能力较好，可参考此[英文链接](https://stackoverflow.com/questions/13596505/python-not-working-in-command-prompt)。

需要提醒的是，添加环境变量时，**一定要添加安装时的安装路径**。有部分学员添加的是“开始”菜单中的路径（路径名包含“Start Menu”，是不正确的）。

## 4.条件语句的简写

以下内容来自[廖雪峰的Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000)

![](https://i.imgur.com/MzIgQAS.png)

## 5.课程3结尾提到的Lab在哪？

目前并没有这个Lab，直接开始下一课的学习即可。英文版课程中对此做了解释（还未完成lab的内容），中文课程没有翻译导致部分学员感到困惑，特此说明。

## 6.pip3 install的正确操作方法

注：这里使用的是pip命令作为示例，实际和pip3操作相同。

![](https://i.imgur.com/GRZUlUd.gif)

## 7.导入BeautifulSoup4时总是显示错误

首先，确认自己安装了包。如果还未安装，请**在命令行**执行如下命令：

```cmd
pip install beautifulsoup4
```

然后**在python文件**中正确导入：

```python
from bs4 import BeautifulSoup
```

请务必注意简写和大小写。

## 8.做项目的时候，明明在Notebook中函数/变量在前面的代码中已经定义了（或者包已经导入了），为什么之后运行的代码要用到之前定义的函数/变量/包还是会提示“Not defined”错误？

很多同学在上次项目没做完，这次重新进入项目的时候，直接从上次未完成的代码块开始写代码并运行，这是**错误的**。当你退出网页（或者刷新）后重新进入项目的时候，Notebook实际上是一片空白的（所有变量、函数、模块等都不存在），必须**从头到尾运行一遍你已完成的所有代码**，才能够继续。

这一点不仅是在线做项目时需要注意的，同样适用于本地Notebook的运行，请务必注意。

# 学习资源推荐

## 中文
1. [菜鸟Python教程（网站）](http://www.runoob.com/python3/python3-tutorial.html)
2. [廖雪峰的Python教程（网站）（数据分析入门学员推荐）](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
3. [Python编程快速上手（书籍）（数据分析入门学员推荐）](https://book.douban.com/subject/26836700/)
4. [计算机科学和Python编程导论（MOOC）](https://www.xuetangx.com/courses/course-v1:MITx+6_00_1x+sp/about)
5. [Python语言程序设计（MOOC）](http://www.icourse163.org/course/BIT-268001)

## 英文
1. [Python for Everybody（MOOC，视频免费，练习收费，部分视频配有中文字幕）](https://zh.coursera.org/specializations/python)
2. [Fundamentals of Computing（MOOC，视频免费，练习收费，大部分视频配有中文字幕）](https://zh.coursera.org/specializations/computer-fundamentals)
3. [DataCamp（数据科学学习网站，课程收费）](https://www.datacamp.com/)
4. [Codecademy（在线交互式编程学习网站，部分内容收费）](https://www.codecademy.com/)

以上资源均为往届数据分析学员推荐或助教本人使用过的资源，质量较高。如果认为学习较为困难，建议使用Udacity课程+上述资源中的任意1-2项搭配学习。

## 英语学习资源推荐

由于绝大部分和编程有关的文档、问答、博客和学习资源均为英文资源，如果缺乏英语能力（这里的英语能力是指，能看懂Python相关库的文档从而了解其用法，能够熟练使用Google、Stackoverflow查询并解决已有问题），对学习编程是非常不利的。在这里推荐一些比较好的英语学习网站，如下：

1. [扇贝网](https://www.shanbay.com/)
2. [考满分](http://www.kmf.com/)

