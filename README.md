# wallhaven
壁纸网站爬虫
1. 安装依赖
```shell
pip install -r requirements.txt
```
2. wallhaven_cc.py
   > 为wallhaven的工具类,参考 [WallhavenApi](https://github.com/Goblenus/WallhavenApi)
3. get_wallpaper.py
   > 基础爬虫程序
   > 
   > 生成的数据路径为当前路径         
   > fg: ./wallpapers/xxx_xxx_xxx_xxx/
   >              
   > 修改路径方法:  在代码的第232-234
   > ![image](https://user-images.githubusercontent.com/44967393/163549220-69bbf617-20b4-47d2-9f10-74d14810e4b0.png)

4. get_wallpaper_Threading.py
   > 加入threading
   > 
   > 生成路径,需要手动指定,可相对路径也可绝对路径
5. img2char.py
   > 输入图片父目录,循环输出路径下的图片字符画
6. tk_window.cpython-37.pyc
   > GUI图形化爬虫工具
   > 需要拷贝一份wallhaven_cc.py 重命名为wallhavenapi.py 
   > 明天我将修复该BUG
