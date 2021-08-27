import environment
import pymysql


def getLinhaMaisVendidaByMesAno(ano, mes):

    myconnection = pymysql.connect(
            host = environment.hostname,
            user = environment.username,
            passwd = environment.password,
            db = environment.database
    )

    with myconnection.cursor() as curs:

        curs.execute("""SELECT
                        id_linha,
                        linha,
                        ano,
                        mes,
                        quantidade_vendida
                FROM vendas.linha_ano_mes
                WHERE ano = %s and mes = %s
                ORDER BY quantidade_vendida desc
                """, (ano, mes))
        
        return curs.fetchone()


def insertTweets(user, text):

        myconnection = pymysql.connect(
                host = environment.hostname,
                user = environment.username,
                passwd = environment.password,
                db = environment.database
        )

        with myconnection.cursor() as curs:
                query = "INSERT INTO vendas.tweets(user_id, text) VALUES(%s, %s)"
                curs.execute(query, (user, text))
                myconnection.commit()