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

5. get_wallpaper_Threading.py
   > 加入threading
   > 
   > 生成路径,需要手动指定,可相对路径也可绝对路径
