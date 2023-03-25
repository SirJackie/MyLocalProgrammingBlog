## 01 - 相对引用

```
报错：https://blog.csdn.net/weixin_43958105/article/details/114012590
Init：https://zhuanlan.zhihu.com/p/115350758?utm_id=0
```

使用`from .Folder.File import Class`而不是`from Folder.File import Class`。

重点在Folder前面的句点符号，标识相对引用，相对于Parent Package的位置引用，而不是相对于文件夹引用。

要在文件夹中创建`__init__.py`，来解决相对引用的报错问题。

## 02 - Multiprocessing 和 Subprocess 库的区别

```
对比：https://blog.csdn.net/yournevermore/article/details/100059404
Win下Main保护：https://www.cnblogs.com/lovefisho/p/16202006.html
Jupyter：https://blog.csdn.net/weixin_56921066/article/details/122155926
```

```
//#coding=utf-8
from multiprocessing import Process
import os
myCmd1='adb logcat -v time>c:/log/ll.txt'
myCmd2='adb shell monkey -p com.yoosal.kanku -s 500 --ignore-crashes --ignore-timeouts --monitor-native-crashes --bugreport --throttle 1000 -v -v -v 100000'
//子进程要执行的代码
def run_proc1(name):
os.system(myCmd1)
def run_proc2():
os.system(myCmd2)
if name== 'main':
p1 = Process(target=run_proc1,args=('test',))
p2 = Process(target=run_proc2)
p1.start()
p2.start()
p1.join()
p2.join()
print('Child process end.')
```

```
import os
import subprocess
myCmd1='adb logcat -v time>c:/log/ll.txt'
myCmd2='adb shell monkey -p com.yoosal.kanku -s 500 --ignore-crashes --ignore-timeouts --monitor-native-crashes --bugreport --throttle 1000 -v -v -v 100000'
child1=subprocess.Popen(myCmd1, shell=True,stdout=None)
child2=subprocess.Popen(myCmd2, shell=True,stdout=None)
```

在Windows中，由于没有fork(Linux中创建进程的机制)，在创建进程的时候会import启动该文件，而在import文件的时候又会再次运行整个文件，如果把Process()放在 `if __name__ == '__main__'` 判断之外，则Process()在被import的时候也会被运行，导致无限递归创建子进程导致报错，所以在Windows系统下，必须把Process()放在 `if __name__ == '__main__'` 的判断保护之下。

在Jupyter Notebook中编写程序，即使处于Windows系统，也不需要 `if __name__ == '__main__'` 的判断保护。Jupyter有内部设计可以规避无限循环问题。

## 03 - Threading 和 _Thread 库的区别

## 04 - 获取操作系统

```
https://www.cnblogs.com/phoenixy/p/17049572.html
```

```
import os
print(os.name)
```

> ```
> posix：对应 linux
> nt：对应 windows
> java：对应 java 虚拟机
> ```