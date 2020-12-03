# yim-test
test



一、软件安装环境

1.java jdk安装，环境配置：https://blog.csdn.net/renlianggee/article/details/90023464

2.python安装，环境配置：https://www.runoob.com/python/python-install.html

3.python IDE安装pycharm：https://www.runoob.com/w3cnote/pycharm-windows-install.html

4.appium和安卓SDK安装配置：https://www.cnblogs.com/soundcode/p/12682366.html

5.mysql安装：https://www.runoob.com/mysql/mysql-install.html

二、安卓adb环境命令操作

1.查看应用包名和当前activity
adb devices
adb shell dumpsys window | findstr mCurrentFocus

2.安装apk
adb install 

3.利用相同wifi环境连接手机
adb tcpip 5555
adb connect 10.12.1.148:5555

4.控件定位工具
4.1、appium自带工具

4.2、旧版本uiautomatorviewer
C:\Users\panbihong\AppData\Local\Android\Sdk\tools\bin


三、自动化测试实施过程

1、打开appium，配置端口号，启动服务

 

2、连接手机，打开手机允许USB调试，adb输入获取连接设备的手机、打开手机测试app获取app包名和activity
adb devices
adb shell dumpsys window | findstr mCurrentFocus

3、再次打开appium，启动session会话，填写手机的信息
      启动会话后等待一会即可看到手机app的页面，轻松定位app的各个控件页面元素

 

 

4、打开Python IDE pycharm，编写测试用例

5、运行测试用例，即可





