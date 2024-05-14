# -*- coding: utf-8 -*-
"""
爬取電影網站資料

Created on 2024-05-11
@author: Tim
"""
import service.ParseNewMovie as ParseNewMovie
import sys
import service.MovieInfoService

def main():
    movie_data = ParseNewMovie.parseMovie()
    service.MovieInfoService.insertMovieInfos(movie_data)
    
if __name__ == '__main__':
    sys.exit(main())