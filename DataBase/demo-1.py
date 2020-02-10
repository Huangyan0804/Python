import pymysql

db = pymysql.connect(
    host="xxx",
    port=xx,
    user="xx",
    passwd="xx",
    db="xx"
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
