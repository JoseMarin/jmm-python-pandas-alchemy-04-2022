from typing import List

import pandas as pd
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float

engine = create_engine('mysql+pymysql://b32d222c298eaa:7ea5271a@eu-cdbr-west-02.cleardb.net/heroku_2140acf9ef7a44b')
Base = declarative_base()


class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)
    precio = Column(Float)
    created_at = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f'{self.id},{self.nombre}, {self.precio},{self.created_at}'


Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    #
    # product1 = Producto(nombre='Portatil', precio=1050.78)
    # product2 = Producto(nombre='Portatil', precio=500.8)
    # product3 = Producto(nombre='SSD 1tb', precio=76.95)
    # product4 = Producto(nombre='HDD 1tb', precio=50.68)
    #
    # session.add(product1)
    # session.add(product2)
    # session.add(product3)
    # session.add(product4)
    #
    # session.commit()

    # SELECT * FROM Productos;
    # productos = session.query(Producto).all()
    # print(productos)

    # SELECT * FROM Productos WHERE id <= 11 and nombre = 'Portatil';
    # productos = session.query(Producto).filter(Producto.id <= 11).filter(Producto.nombre == 'Portatil')
    # print(productos)


    # id = []
    # nombre = []
    # precio = []
    # created_at = []
    #
    # data = {
    #     "id": id,
    #     "nombre": nombre,
    #     "precio": precio,
    #     "created_at": created_at
    # }
    #
    # for pro in productos:
    #     id.append(pro.id)
    #     nombre.append(pro.nombre)
    #     precio.append(pro.precio)
    #     created_at.append(pro.created_at)
    #
    #
    # df_productos = pd.DataFrame(data)
    # df_productos.set_index('id', inplace=True)
    # print(df_productos)
    #
    # df_productos.to_csv('../data/df_productos.csv', header=False, index=True)


    # SELECT * FROM Productos;
    # productos = session.query(Producto.id, Producto.nombre, Producto.precio, Producto.created_at).all()
    # print(productos)
    #
    # df_productos = pd.DataFrame(productos, columns=['id','nombre','precio','created_at'])
    # df_productos.set_index('id', inplace=True)
    # print(df_productos)
    #
    # df_productos.to_csv('../data/df_productos.csv', header=False, index=True)

    # SELECT * FROM Productos WHERE id = 11;
    productos = session.query(Producto.id, Producto.nombre, Producto.precio, Producto.created_at).filter(
        Producto.id == 11
    )

    print(productos)

    df_productos = pd.DataFrame(productos, columns=['id', 'nombre', 'precio', 'created_at'])
    df_productos.set_index('id', inplace=True)
    print(df_productos)
    #
    df_productos.to_csv('../data/df_productos.csv', header=False, index=True)

    # Export from dataframe to BBDD
    df_productos.to_sql('products', engine, if_exists='replace', index=False)
    #
    # # # Import from SQL to dataframe
    # sql_query = pd.read_sql_query('''
    #                                SELECT
    #                                *
    #                                FROM productos
    #                                ''', engine)
    #
    # df = pd.DataFrame(sql_query, columns=['id', 'nombre', 'precio', 'created_at'])
    # df.set_index('id', inplace=True)
    # print(df)

