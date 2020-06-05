# 动物餐厅 微信小程序
适用于windows客户端微信小程序动物餐厅
自动点击宣传按钮，自动点菜，自动点击座位特殊顾客
```
pip install -r requirements.txt
python animal.py
```
模拟鼠标点击各个按钮，程序运行期间无法使用鼠标光标，按ESC键退出程序

release中包含使用nuitka打包的win32可执行程序，解压打开animal.exe即可运行

nuitka打包示例
```
nuitka --mingw64 --standalone --show-progress --show-memory --recurse-all --output-dir=out --plugin-enable=multiprocessing --windows-disable-console animal.py
```
