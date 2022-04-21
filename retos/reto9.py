from typing import List

import pandas as pd
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float


emisiones_2016 = pd.read_csv('../data/emisiones-2016.csv', sep = ';')
emisiones_2017 = pd.read_csv('../data/emisiones-2017.csv', sep = ';')
emisiones_2018 = pd.read_csv('../data/emisiones-2018.csv', sep = ';')
emisiones_2019 = pd.read_csv('../data/emisiones-2019.csv', sep = ';')

emisiones = pd.concat([emisiones_2016, emisiones_2017, emisiones_2018, emisiones_2019])

df_emisiones = emisiones[['PROVINCIA', 'MUNICIPIO','ESTACION','D30']]



engine = create_engine('mysql+pymysql://b32d222c298eaa:7ea5271a@eu-cdbr-west-02.cleardb.net/heroku_2140acf9ef7a44b')
Base = declarative_base()


class Emisiones(Base):
    __tablename__ = 'emisiones_geeksHubs'

    id = Column(Integer, primary_key=True)
    PROVINCIA = Column(Integer)
    MUNICIPIO = Column(Integer)
    ESTACION = Column(Integer)
    D30 = Column(Float)
    created_at = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f'{self.id},{self.PROVINCIA},{self.MUNICIPIO},{self.ESTACION},{self.D30}'


Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    print(emisiones)
    print(df_emisiones)

    # Export from dataframe to BBDD
    df_emisiones.to_sql('emisiones_geeksHubs'.lower(), engine, if_exists='append', index=False)