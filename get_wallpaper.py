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
import re


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


def get_url(base_url):
    keyword = input("请输入英文关键词:(爬取排行榜请输入toplist)")
    if keyword == 'toplist':
        base_url = base_url + keyword + '?page='
    else:
        base_url = base_url + 'search?q=' + keyword + '&page='
    return base_url


def get_img_url(base_url):
    print('获取img_url,开始时间', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    start_time = time.time()
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    }
    img_url_list = []
    temp_url = base_url + "&page=2"
    page_number_str = requests.get(url=temp_url, headers=header).text
    re_page = '<h2>Page <span class="thumb-listing-page-num">\d</span>\D/\D\d+'
    total_number = str(re.findall(re_page, page_number_str, re.S)).split('/')[-1][:-2].strip()
    page_num = input(f"该类型下共有{total_number}页,一页24张图片,请输入需要爬取的图片页数:")
    print(f"您要爬取的页数是{page_num}页!")
    for num in range(1, int(page_num) + 1):
        new_url = base_url + "&page=" + str(num)
        page_text = requests.get(url=new_url, headers=header).text
        ex = '<a class="preview" href="(.*?)"'
        img_url_list += re.findall(ex, page_text, re.S)
    print('获取img_url,用时', str(time.time() - start_time), "秒")
    return img_url_list


def download_img(img_url_list):
    start_time = time.time()
    print('开始下载图片,开始时间', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    }
    keyword = input("请再次输入关键词以方便创建文件夹:")
    if not os.path.exists('./wallpapers'):
        os.mkdir('./wallpapers')
    path = './wallpapers/' + keyword
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(len(img_url_list)):
        x = img_url_list[i].split('/')[-1]
        a = x[0] + x[1]
        img_url = 'https://w.wallhaven.cc/full/' + a + '/wallhaven-' + x + '.jpg'
        # 'https://w.wallhaven.cc/fully/wallhaven-j.jpg'
        try:
            start_time_time = time.time()
            code = requests.get(url=img_url, headers=header).status_code
            if code == 404:
                img_url = 'https://w.wallhaven.cc/full/' + a + '/wallhaven-' + x + '.png'
            img_data = requests.get(url=img_url, headers=header, timeout=40).content
            img_name = img_url.split('-')[-1]
            img_path = path + '/' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功', '用时', "{:.3f}".format(time.time() - start_time_time), '秒')
        except Exception as e:
            print(e)
    print('下载图片完成,总用时', "{:.3f}".format(time.time() - start_time), "秒!")


def main():
    # base_url=get_url(url)
    categories, purity, topRange, sorting = get_pram()
    base_url = f"https://wallhaven.cc/search?categories={categories}&purity={purity}&topRange={topRange}&sorting={sorting}&order=desc"
    img_url_list = get_img_url(base_url)
    download_img(img_url_list)


def save_file(cate, purities, top_ran, sor_ting, data_dict, current_page):
    start_time = time.time()
    filepath = "_".join([cate, purities, top_ran, sor_ting])
    print("filepath ===", str(filepath))
    print('开始下载图片,开始时间', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    }

    if not os.path.exists('/var/www/html/wallpapers'):
        os.mkdir('/var/www/html/wallpapers')
    path = '/var/www/html/wallpapers/' + filepath
    if not os.path.exists(path):
        os.mkdir(path)
    for data in data_dict['data'][:int(current_page) * 24]:
        try:
            start_time_time = time.time()
            img_data = requests.get(url=data['path'], headers=header, timeout=40).content
            img_name = data['path'].split("/")[-1].split("-")[-1]
            img_path = path + '/' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功', '用时', "{:.3f}".format(time.time() - start_time_time), '秒')
        except Exception as e:
            print(e)
    print('下载图片完成,总用时', "{:.3f}".format(time.time() - start_time), "秒!")


def run_main():
    api_key, categories, purity, topRange, sorting = get_pram()
    wall = WallhavenApiV1(api_key=api_key)
    res_data = wall.search(categories=categories, purities=purity, sorting=sorting, top_range=topRange)
    total_page = res_data['meta']['last_page']
    # 写入保存方法
    current_pageNumber = int(input(f"当前类别的壁纸总页数有{total_page}页,请输入要抓取的页面数\r\n"))
    current_page = 0
    if Decimal(current_pageNumber).compare(Decimal(total_page)) == -1:
        current_page = current_pageNumber
    else:
        current_page = total_page
    try:
        for page in range(1, current_page + 1):
            res_data = wall.search(categories=categories, purities=purity, sorting=sorting, top_range=topRange,
                                   page=str(page), seed=1)
            print(res_data)
            save_file(categories.value, purity.value, topRange.value, sorting.value, res_data, current_page)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run_main()
