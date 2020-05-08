## python 调试debug方法

1. print输出日志方式

2. logging记录日志方式，优点是可输出到日志文件中，方便后续查看

3. assert断言方式，在预感要出错的地方
```python
s = 1
assert s == 0, "s is not zero"
```
可在运行期间指定 -O，去除assert执行，此时assert预计认为pass
```shell script
python -O debug.py
```

4. pdb调试
- 执行python时设置pdb模式, 1命令查看代码，n单步执行，p 变量名 查看变量，q结束调试
```shell script
python -m pdb debug.py
```

- 代码中设置pdb.set_trace(),在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
p 变量名查看变量值，c继续执行
```python
import pdb

if __name__ == '__main__':
    s = 1 + 2
    pdb.set_trace()
    s = 0
```

5. IDE debug断点执行