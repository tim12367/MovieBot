import dao.MovieInfoDao
import pandas as pd

def insertMovieInfos(movie_data_listMap) :
    movie_dataFrame = pd.DataFrame(movie_data_listMap)
    dao.MovieInfoDao.insertMovieInfos(movie_dataFrame)