# -*- encoding : utf-8 -*-
"""
@Time : 2022年04月14日 12:55
@Contact : hfhzzdx@hotmail.com
@File : get_wallpaper.py
@SoftWare : PyCharm
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022-04-14 12:55   hfh      1.0         None
"""

from datetime import datetime
from decimal import *
from wallhaven_cc import *
from threading import Thread, Lock
from queue import Queue
import threading

q = Queue()
lock = Lock()
ua_list = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    ' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1',
    ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]


def if_login():
    login_id = str(input("请选择是否登录\r\n1.登录(输入y确定)     2.不登陆(输入除y以外的任意字符)\r\n"))
    if login_id == 'y' or login_id == 'Y':
        api_key = input("请输入个人Api Key,详情请查看 https://wallhaven.cc/settings/account\r\n")
        return True, api_key
    else:
        return False, ''


def get_pram():
    is_login, api_key = if_login()
    categories = ""
    purity = ""
    topRange = ""
    sorting = ""
    while True:
        category = str(input("请输入要爬取的类别:\r\n1.普通 2.动漫 3.人物\r\n"))
        if category != '1' and category != '2' and category != '3':
            print("输入有误,请重新输入!")
            continue
        elif category == '1':
            print("您要爬取的类型是:1.普通类别")
            categories = Category.general
            break
        elif category == '2':
            print("您要爬取的类型是:2.动漫类别")
            categories = Category.anime
            break
        elif category == '3':
            print("您要爬取的类型是:3.人物类别")
            categories = Category.people
            break
    while True:
        if is_login:
            wall_level = str(input("请输入要爬取的壁纸级别:\r\n1.SFW 2.R18+ 3.限制级\r\n"))
            if wall_level != '1' and wall_level != '2' and wall_level != '3':
                print("输入有误,请重新输入!")
                continue
            elif wall_level == '1':
                print("您要爬取的级别是:1.适用于工作场合")
                purity = Purity.sfw
                break
            elif wall_level == '2':
                print("您要爬取的级别是:2.R18+")
                purity = Purity.sketchy
                break
            elif wall_level == '3':
                print("您要爬取的级别是:3.限制级")
                purity = Purity.nsfw
                break
        else:
            wall_level = str(input("请输入要爬取的壁纸级别:\r\n1.GFW 2.R18+\r\n"))
            if wall_level != '1' and wall_level != '2':
                print("输入有误,请重新输入!")
                continue
            elif wall_level == '1':
                print("您要爬取的级别是:1.适用于工作场合")
                purity = Purity.sfw
                break
            elif wall_level == '2':
                print("您要爬取的级别是:2.R18+")
                purity = Purity.sketchy
                break
    while True:
        crawl_time = str(input("请输入要爬取的时间段:\r\n1.一天前 2.三天前 3.一周前 4.一月前 5.三月前 6.六月前 7.一年前\r\n"))
        if crawl_time != '1' and crawl_time != '2' and crawl_time != '3' and crawl_time != '4' and crawl_time != '5' and crawl_time != '6' and crawl_time != '7':
            print("输入有误,请重新输入")
            continue
        elif crawl_time == '1':
            print("您爬取的时间段是:1.一天前")
            topRange = TopRange.one_day
            break
        elif crawl_time == '2':
            print("您爬取的时间段是:2.三天前")
            topRange = TopRange.three_days
            break
        elif crawl_time == '3':
            print("您爬取的时间段是:3.一周前")
            topRange = TopRange.one_week
            break
        elif crawl_time == '4':
            print("您爬取的时间段是:4.一月前")
            topRange = TopRange.one_month
            break
        elif crawl_time == '5':
            print("您爬取的时间段是:5.三月前")
            topRange = TopRange.three_months
            break
        elif crawl_time == '6':
            print("您爬取的时间段是:6.六月前")
            topRange = TopRange.six_months
            break
        elif crawl_time == '7':
            print("您爬取的时间段是:7.一年前")
            topRange = TopRange.one_year
            break
    while True:
        sort_by = str(input("请输入要爬取的排序方式:\r\n1.默认排序 2.随机排序 3.日期排序 4.次数排序 5.喜爱排序 6.榜单排序 7.热度排序\r\n"))
        if sort_by != '1' and sort_by != '2' and sort_by != '3' and sort_by != '4' and sort_by != '5' and sort_by != '6' and sort_by != '7':
            # [relevance,random,date_added,views,favorites,toplist,hot]
            print("输入有误,请重新输入")
            continue
        elif sort_by == '1':
            print("您爬取的排序方式是:1.默认排序")
            sorting = Sorting.relevance
            break
        elif sort_by == '2':
            print("您爬取的排序方式是:2.随机排序")
            sorting = Sorting.random
            break
        elif sort_by == '3':
            print("您爬取的排序方式是:3.日期排序")
            sorting = Sorting.date_added
            break
        elif sort_by == '4':
            print("您爬取的排序方式是:4.次数排序")
            sorting = Sorting.views
            break
        elif sort_by == '5':
            print("您爬取的排序方式是:5.喜爱排序")
            sorting = Sorting.favorites
            break
        elif sort_by == '6':
            print("您爬取的排序方式是:6.榜单排序")
            sorting = Sorting.toplist
            break
        elif sort_by == '7':
            print("您爬取的排序方式是:7.热度热度排序")
            sorting = Sorting.hot
            break
    return api_key, categories, purity, topRange, sorting


def download_img(path):
    while True:
        # 判断队列不为空则执行，否则终止
        if not q.empty():
            url = q.get()
            # print("多线程download_img url===", str(url))
            start_time = time.time()
            try:
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
                }
                img_data = requests.get(url=url, headers=headers, timeout=40).content
                # print("headers====", str(headers))
                # 写入数据
                # url = 'https://w.wallhaven.cc/full/yj/wallhaven-yj7k5l.jpg'
                img_name = url.split("/")[-1].split("-")[-1]
                img_path = path + '/' + img_name
                with open(img_path, 'wb') as fp:
                    fp.write(img_data)
                    lock.acquire()
                    lock.release()
                    fp.close()
                print(img_name, '下载成功', '用时', "{:.3f}".format(time.time() - start_time), '秒')
            except Exception as e:
                print(e)
        else:
            break


def mkdir_dir(os_path, cate, purities, top_ran, sor_ting):
    base_path = os_path + '/wallpapers/'
    filepath = "_".join([cate, purities, top_ran, sor_ting])
    print('创建文件夹路径,开始时间', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    path = base_path + filepath
    if not os.path.exists(path):
        os.mkdir(path)
    # for data in data_dict['data']:
    #     # 将url加入队列
    #     que_list.append(data)
    # # 放入queue
    # print("mkdir_dir  que_list==",str(len(que_list)))
    # for url in que_list:
    #     q.put(url)
    # print(q.maxsize)
    # try:
    #     t_list = []
    #     # 创建多线程
    #     for i in range(current_page*24):
    #         t = Thread(target=download_img(q, path))
    #         t_list.append(t)
    #         t.start()
    #     for tt in t_list:
    #         tt.join()
    # except Exception as e:
    #     print(e)
    # print('下载图片完成,总用时', "{:.3f}".format(time.time() - start_time), "秒!")
    return path


def run_main():
    res_list = []
    api_key, categories, purity, topRange, sorting = get_pram()
    wall = WallhavenApiV1(api_key=api_key)
    try:
        res_data = wall.search(categories=categories, purities=purity, sorting=sorting, top_range=topRange)
    except Exception as e:
        print(e)
    total_page = res_data['meta']['last_page']

    current_pageNumber = int(input(f"当前类别的壁纸总页数有{total_page}页,请输入要抓取的页面数\r\n"))
    dirname = input("请输入要保留图片的路径\r\n")
    path = mkdir_dir(dirname, categories.value, purity.value, topRange.value, sorting.value)
    current_page = 0
    if Decimal(current_pageNumber).compare(Decimal(total_page)) == -1:
        current_page = current_pageNumber
    else:
        current_page = total_page

    try:
        for page in range(1, current_page + 1):
            res = wall.search(categories=categories, purities=purity, sorting=sorting, top_range=topRange, page=page)
            res_list.append(res['data'])
        print("抓取到的总页数为:", str(len(res_list)))
        print("抓取到的总图片数为:", str(len(res_list)*24))
        # 加入队列
        for data in res_list:
            for img_url in data:
                # 取下载url
                q.put(img_url['path'])
    except Exception as e:
        print(e)




    # 多线程保存
    print("开始多线程保存,当前时间为,",datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    start_time = time.time()
    t_list = []
    for i in range(5):
        t = Thread(target=download_img(path))
        t_list.append(t)
        t.start()
    for t in t_list:
        t.join()
    print("任务完成,总用时", "{:.3f}".format(time.time() - start_time), '秒')


if __name__ == '__main__':
    run_main()

