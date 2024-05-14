from sqlalchemy import create_engine

def insertMovieInfos(movie_info_dataFrame) :
    # 資料庫連線
    engine = create_engine('mysql+pymysql://root:1234@localhost/movie_bot?charset=utf8')
    # 寫入DB
    movie_info_dataFrame.to_sql('movie_info', engine, schema = 'movie_bot', if_exists='append', index=False)