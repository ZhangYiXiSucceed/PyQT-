>环境：<font color=red>**Pycharm IDE+PtQT+Qt designer**</font>

## 第一步 安装环境

&emsp;&emsp;需要安装python下qt的环境及工具，<font color=red>**终端terminal下面运行指令**</font>，我这里已经安装，所以显示已经有了，两个都需要安装，需要记住安装的位置，一会儿需要设置环境变量。
```python
pip install PyQt5
pip install PyQt5-tools
```

```python
(DemoProject) E:\WorkSpace\BT\DemoProject>pip install PyQt5
Requirement already satisfied: PyQt5 in c:\users\guoqing.zhang\appdata\local\programs\python\python37\lib\site-packages (5.1
5.2)
Requirement already satisfied: PyQt5-sip<13,>=12.8 in c:\users\guoqing.zhang\appdata\local\programs\python\python37\lib\site
-packages (from PyQt5) (12.8.1)

```


配置<font color=red>**qt designer.exe环境变量**</font>，根据自己安装的目录选择
目录：C:\Users\guoqing.zhang\AppData\Local\Programs\Python\Python37\Lib\site-packages\qt5_applications\Qt\bin   
	
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308160043879.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NDMwMzcx,size_16,color_FFFFFF,t_70#pic_center)

## 第二步 Pycharm配置外部工具	
	
&emsp;&emsp;打开Pycharm，点击File-->Setting-->Tools-->External Tools，选择+号新建，第一个是qt designer，program为路径，arguments不填，working directory 为工作路径，填 $ FileDir $，为当前工作目录，这个工具可以<font color=red>**直接打开qt designer**</font>（qt 设计师）。
	
![在这里插入图片描述](https://img-blog.csdnimg.cn/202103081601196.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NDMwMzcx,size_16,color_FFFFFF,t_70#pic_center)

&emsp;&emsp;第二个是PyUIC，program为python路径，arguments 填：-m PyQt5.uic.pyuic $ FileName $ -o $FileName，可以<font color=red>**将UI文件转换为python代码**</font>，注意FileName前后没有空格。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308160128305.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NDMwMzcx,size_16,color_FFFFFF,t_70#pic_center)

## 第三步 qt界面设计

+ <font color=red>**可以使用代码进行绘制**</font>

```python
    self.Seed = QLineEdit()
    self.DescriptionSeed = QLabel()
    self.Key = QLineEdit()
    self.DescriptionKey = QLabel()
    self.DescriptionSeed.setText('Seed')
    self.DescriptionKey.setText('Key')
    self.Seed.setFixedWidth(200)
    self.Seed.setFixedHeight(25)
    self.Key.setFixedHeight(25)
    self.Key.setFixedWidth(200)
    self.Seed.setPlaceholderText('例如：0D 4A 1F FE')
```


![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308162942549.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NDMwMzcx,size_16,color_FFFFFF,t_70#pic_center)

几个函数介绍一下
1. setFixedSize，设置控件大小
2. QHBoxLayout，QVBoxLayout，控件横纵摆放函数
3. addWidget，添加控件函数
4. addLayout，添加布局函数
5. QGroupBox，管理布局的组管理函数
6. setLayout，设置布局，就可以显示出控件

+ <font color=red>**也可以直接使用qt designer 进行绘制**</font>

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308162934370.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NDMwMzcx,size_16,color_FFFFFF,t_70#pic_center)


## 第四步打包生成exe文件

终端 terminal 下面运行指令：
&emsp;&emsp;<font color=red>**pyinstaller -F -w win.py**</font>, 
运行完成之后，工程目录中会有dist的文件夹，里面有exe问可执行文件。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308162146826.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NDMwMzcx,size_16,color_FFFFFF,t_70#pic_center)

><font color=blue>**碰到的问题**</font>：Pycharm  右键菜单选项里面没有external tools

><font color=blue>**解决办法**</font>：<font color=red>**复制Link或者path**</font>（如下图所示），然后到IDE界面显示工程文件的区域粘贴，反复尝试几次，然后重新打开就有了
>
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308162023129.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NDMwMzcx,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308162043846.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NDMwMzcx,size_16,color_FFFFFF,t_70#pic_center)

## 关于本项目
+ 项目作者：ZGQ
+ 邮箱：Guoqingzhang0813@163.com
+ 开发环境：PtQT5 版本5..15,Qt_Designer,Python 3.7
+ 适用平台：WIndow、

