import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='gashaimpactdb')

personagens: list = [
    ('Mona', 'Hydro', 5),
    ('Barbara', 'Hydro', 4),
    ('Kamisato Ayato', 'Hydro', 5),
    ('Sangonomiya Kokomi', 'Hydro', 5),
    ('Tartaglia', 'Hydro', 5),
    ('Xingqiu', 'Hydro', 4),
    ('Jean', 'Anemo', 5),
    ('Kaedehara Kazuha', 'Anemo', 5),
    ('Sayu', 'Anemo', 4),
    ('Sucrose', 'Anemo', 4),
    ('Venti', 'Anemo', 5),
    ('Xiao', 'Anemo', 5),
    ('Aloy', 'Cryo', 5),
    ('Chongyun', 'Cryo', 4),
    ('Diona', 'Cryo', 4),
    ('Eula', 'Cryo', 5),
    ('Ganyu', 'Cryo', 5),
    ('Kaeya', 'Cryo', 4),
    ('Kamisato Ayaka', 'Cryo', 5),
    ('Qiqi', 'Cryo', 5),
    ('Rosaria', 'Cryo', 4),
    ('Shenhe', 'Cryo', 5),
    ('Beidou', 'Electro', 4),
    ('Fischl', 'Electro', 4),
    ('Keqing', 'Electro', 5),
    ('Kujou Sara', 'Electro', 4),
    ('Lisa', 'Electro', 4),
    ('Razor', 'Electro', 4),
    ('Shogun Raiden', 'Electro', 5),
    ('Yae Miko', 'Electro', 5),
    ('Albedo', 'Geo', 5),
    ('Arataki Itto', 'Geo', 5),
    ('Gorou', 'Geo', 4),
    ('Ningguang', 'Geo', 4),
    ('Noelle', 'Geo', 4),
    ('Yunjin', 'Geo', 4),
    ('Zhongli', 'Geo', 4),
    ('Amber', 'Pyro', 4),
    ('Bennett', 'Pyro', 4),
    ('Hutao', 'Pyro', 5),
    ('Klee', 'Pyro', 5),
    ('Thoma', 'Pyro', 4),
    ('Xiagling', 'Pyro', 4),
    ('Xinyan', 'Pyro', 4),
    ('Yanfei', 'Pyro', 4),
    ('Yoimiya', 'Pyro', 5),
    ('Diluc', 'Pyro', 5)
]

def AtualizarPersonagensDB():
    query = ("INSERT INTO PERSONAGEM "
             "(NOME, TIPO, ESTRELA) "
             "VALUES (%s, %s, %s)")

    conn = cnx.cursor();

    for personagem in personagens:
        conn.execute(query, personagem)

    cnx.commit()
    cnx.close()

##AtualizarPersonagensDB()