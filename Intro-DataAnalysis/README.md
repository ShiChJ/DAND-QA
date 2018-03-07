# P3常见问题汇总

## 课程及项目常见问题答疑

**1. 课程练习是否有答案？**

见本页面对应的L1/L2/L3三个文件夹。需要注意的是，绝大部分答案是助教自己做的，虽然基本可以保证答案正确，但**不一定是最优的实现方法**。如果你有更好的代码建议或实现方案，欢迎在社群内分享。

查看答案后如果仍希望知道自己代码报错的原因或答案代码的逻辑，处理原则同P2：

在经过以上步骤，仍然不知道代码（包括做项目时和项目有关的代码）的出错原因或者某段答案代码的逻辑，请在通关群提供以下信息并@助教，并描述问题。
  - 练习对应的课程章节；
  - 练习界面的截图（如果代码报错，请务必将报错信息全部截图）；
  - 文本格式的代码（从练习界面复制，粘贴到聊天框发送）。
  - **注意**：如果希望解决**自己写的代码中的疑问**，在提供以上信息的同时，最好能说明自己解决问题思路和疑惑的地方，以便助教更好定位你的知识盲点并提供相应建议。仅仅问一句“为什么我的代码不对”并不是推荐的提问方式，因为**重要的不是正确与否，而是实现思路**。直接指出错误并告诉正确答案当然很容易，但对于学员而言，以后实际工作中如果遇到类似问题，没有正确的思路还是无法解决，这点敬请理解。

**2. 如何将上一节练习生成的数据导入到下一节的Workspace中？**

请参考本页面的.mp4视频文件“Workspace中导入上一节生成的数据.mp4”。

**3. 课程1-15节“评估和理解”练习中，“有多少教育的唯一值”是什么意思？**

意思是“教育的可能取值的数量”。例如，假设数据集中教育一共有5类：小学、初中、高中、大学、其他。则“教育的唯一值”为5。

**4. 为什么做在线练习时，加载数据会报错，提示数据不存在（not exist错误）？**

请注意，P3课程的大部分练习，数据**都需要自行导入**。具体操作方法为，找到上一节练习，下载对应数据，导入到这一节的工作环境。如果上一节练习没有对应数据，请往回多翻几个练习，总能够找到相关数据，不存在数据缺失的问题（助教亲测）。至于如何下载、导入数据，见本节问题2。

**5. 关于“偏度”“左偏”“右偏”（Skewed）的解释：**

来自维基百科：

![](https://i.imgur.com/PFC3FEb.png)

## 在本地环境做练习和项目时可能遇到的问题及答疑汇总

**1. Conda更新很慢/包下载很慢/出现Time Out错误或类似提示等**

用以下任一种方法可以解决：

- 翻墙（自行搜索软件下载，或者和助教联系）；
- 使用清华大学提供的镜像源，具体操作方式见[此链接](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/)

**2. 如何同时安装Python3和Python2？**

Conda支持安装多个Python环境，具体操作方式见[此链接](https://conda.io/docs/py2or3.html)

**3. 为什么装了多个环境，Jupyter Notebook还是只能使用一个版本的Python？**

请检查你是否在所有环境中安装了Jupyter Notebook，具体方式如下：

1. 打开Anaconda Navigator
 ![](https://i.imgur.com/xHULooG.png)

2. 在Navigator中做如下操作
 ![](https://i.imgur.com/6vi81LS.png)

3. 重新打开Notebook，即可使用两个版本的环境


**4. 命令行是什么？如何在命令行转换目录？**

由于命令行不是本课程的教学内容，所有命令行相关的疑问均请参见[此链接](https://blog.henix.info/blog/windows-cmdbasic/_.html)

**6. 在命令行和Anaconda Prompt中都无法使用Conda命令的所有解决方案。**

- 检查系统版本。Anaconda已经不支持Windows XP；同时查看自己电脑是32位还是64位（本页面视频有说明），不要装错了；
- 检查自己是否原来安装过Python，如果安装过请彻底删除Python（同时要删除环境变量）后重装Anaconda；
- 检查自己是否将Conda命令添加到了环境变量，操作方法见[本页面](https://stackoverflow.com/questions/28612500/why-anaconda-does-not-recognize-conda-command)；
- 确保你的Anaconda安装路径不包含中文或其他非英语常用字符；
- 经过以上步骤还是没有任何改善，请卸载Anaconda重装一遍；
- 重装一遍后还是没有改善，说明助教也不知道原因，无法帮助你，所以不用在群里@助教了，直接使用微软出品的[Azure Notebook](https://notebooks.azure.com/)作为替代方案完成课程和项目。

**7. Mac系统下无法安装matplotlib，提示“Failed building wheel for subprocess32”**

安装[Xcode](https://developer.apple.com/xcode/)

**8. 安装Anaconda时显示UnicodeDecodeError。**

- 如果Python是2.7版本的，请确保安装路径没有中文或者其他非英语常用字符；
- 如果安装路径不存在上述问题，请参考[此链接](http://www.cnblogs.com/kangronghu/p/6154919.html)解决。

**9. 如何正确下载Notebook？**

1. 右键另存为，将文件存入任一文件夹；
2. 更改文件夹后缀名为.ipynb。如果无法修改，请在文件管理器中勾选下图的“文件扩展名”，再对文件重命名，直接修改后缀。最终你的文件名为“xxxx.ipynb”

![](https://i.imgur.com/IYUCKqb.png)


**10. 两个简明的[Anaconda](https://www.zhihu.com/question/58033789/answer/254673663)和[Jupyter Notebook](https://www.zhihu.com/question/46309360/answer/254638807)使用教程（感谢学员悟空和知乎用户“猴子”提供的链接及教程内容）**

**11. 在Jupyter Notebook中按Tab键无法自动补全代码。**

请尝试安装pyreadline包，命令如下：

```cmd
conda install pyreadline
```

再打开Notebook重试补全代码功能。

**12. 明明已经使用命令安装了某个包（比如Unicodecsv），在Notebook导入时却显示No module named XXX错误。**

目前还没有根本性的解决办法，可能是环境变量的问题导致。一个可行的方案是创建新环境，并与Notebook关联，所有代码都在新环境中运行。具体步骤如下：

假如你第一次安装Anaconda，系统会自动创建一个默认环境，Notebook中也只有默认环境。默认环境中包无法导入时，请尝试如下命令（假设你的Python版本为2.7）：

```cmd

conda create -n py27 python=2.7 anaconda #创建环境，py27可以是其他名称
conda install nb_conda
acitvate py27 #进入新环境
conda install unicodecsv #在新环境中安装模块

```

然后再启动jupyter notebook，做如下操作：

![](https://i.imgur.com/hb1iqv0.png)

点击Python [conda env: py27]，切换到py27环境，再运行代码看下能否导入模块。

请注意，以后进入所有notebook的时候，都需要切换到py27环境。你安装所有包时，都需要先使用activate py27命令，在新环境中安装。

**13. 在Mac环境下运行Jupyter Notebook报如下错误：**

![](https://i.imgur.com/z5IRAeV.jpg)

解决办法：使用此命令启动Jupyter Notebook：

```cmd
jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000000
```

**14. 运行Conda命令时出现“Missing write permissions”错误：**

请使用如下方式打开Anaconda Prompt，再次运行Conda命令：

![](https://i.imgur.com/V5HdRn2.png)

**15. 有没有其他数据分析相关的书籍和学习资料？**

链接：https://pan.baidu.com/s/1eUfFebK 密码：wio6

网盘内容会不定期更新。注意，**请不要用微信自带的浏览器打开**，否则会显示链接不存在。



