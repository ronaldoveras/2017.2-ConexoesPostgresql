import psycopg2
import csv, sys
import datetime
import logging
try:

    #Criando a conexão ao banco
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
    print("Conectado ao banco")
    #Definindo um cursor para execuções
    cur = conn.cursor()
    cur.execute("INSERT INTO ESTACIONAMENTO VALUES (%s, %s, %s, %s)",(8, 1, "11/10/2017 06:36", "11/10/2017 18:48:27"));
    conn.commit();

    consulta ="SELECT * FROM ESTACIONAMENTO ORDER BY codigoestacionamento"
    cur.execute(consulta)
    rows = cur.fetchall()
    for row in rows:
        print('Estacionamento: ' + str(row[0]))
        print('Veículo: ' + str(row[1]))
        if row[2] is not None:
            print('Data Entrada: ' + row[2].strftime('%d/%m/%Y'))
        if row[3] is not None:
            print('Data Saída: ' + row[3].strftime('%d/%m/%Y'))
except Exception as ex:
    logging.exception('Infelizmente aconteceu alguma besteira')

                        
