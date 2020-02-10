import pymysql

db = pymysql.connect(
    host="172.96.202.192",
    port=3306,
    user="root",
    passwd="Zsqfhy0804#",
    db="mydatabase"
)

cursor = db.cursor()

sql = """
create table myscore(
    cid varchar(20)  not null, 
    cname varchar(20) not null,
    score int not null,
    primary key(cid)
)    DEFAULT CHARSET=utf8;
"""

try:
    cursor.execute(sql)
    db.commit()
    print('yes')
except:
    db.rollback()
    print('no')


# 关闭数据库连接
db.close()