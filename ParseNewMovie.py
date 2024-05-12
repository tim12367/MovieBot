# -*- coding: utf-8 -*-
"""
爬取電影網站資料

Created on 2024-05-11
@author: Tim
"""
from pyquery import PyQuery as pq
import time

def __getTimeStamp():
    local_time = time.localtime()  # 取得時間元組
    timeString = time.strftime("%Y-%m-%d-%H.%M.%S", local_time)  # 轉成想要的字串形式
    return timeString


def __parseMovieDetail(link):
    movie_detail = {}

    query = pq(link, encoding='utf8')
    film_title = pq(query('.filmTitle')[0]).text()
    movie_detail['film_title'] = film_title
    print('電影名稱:' + film_title)

    if query('.runtime li').length > 1:  # 若大於一筆代表有片長
        movie_length = pq(query('.runtime li')[0]).text().strip('片長：').strip('分')
        movie_detail['movie_length'] = movie_length
        print('片長:' + movie_length)

        release_date = pq(query('.runtime li')[1]).text().strip('上映日期：').replace('/', '-')
        movie_detail['release_date'] = release_date
        print('上映日期:' + release_date)

    elif query('.runtime li').length > 0:
        print('片長:' + '無資料')

        release_date = pq(query('.runtime li')[0]).text().strip('上映日期：').replace('/', '-')
        movie_detail['release_date'] = release_date
        print('上映日期:' + release_date)
    return movie_detail

"""
爬取電影資料
"""
def parseMovie() :
    # 電影連結
    new_movie = 'http://www.atmovies.com.tw/movie/next/0/'
    root_domain = 'http://www.atmovies.com.tw'

    query = pq(new_movie, encoding='utf8')  # 用UTF8開啟爬到的資料

    # check是否有資料
    if not query:
        raise ValueError(f'[{__getTimeStamp()}] 網頁抓取錯誤: {new_movie}')

    # 爬取畫面上所有電影
    index = 1  # 總共有幾部電影
    links = []
    for film_list_element in query('.filmListAll li'):
        film_list = pq(film_list_element)  # 重新解析元素
        title = film_list('.filmtitle').text()  # 電影標題
        link = root_domain + film_list('a').attr('href')  # 電影詳情連結
        links.append(link)
        print(index)
        print(title)
        print(link)
        index += 1

    # 爬取電影詳情頁
    movie_details = []
    for link in links:
        try:
            movie_detail = __parseMovieDetail(link)
            movie_details.append(movie_detail)
        except Exception as e:
            print("爬取電影詳情頁發生錯誤!", e)
        time.sleep(3)

    print(movie_details)
    return movie_details