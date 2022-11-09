import pymysql

#数据库连接
con = pymysql.connect(host='127.0.0.1',port='2222',user='root',password='admin',database='LIB1')
# host：数据库地址
# port：端口
# user：登录名
# password：密码
# database：数据库名
# 用游标操作数据库 创建游标
cur = con.cursor()
# 写数据库语句
sql = 'select * from table1'
# 执行语句
cur.execute(sql)

# 获取查询语句的结果,fetchall
result = cur.fetchall() # 获取所有结果
# result = cur.fetchone() # 获取一条结果
# result = cur.fetchmany()    # 获取n条结果，fetchmany(条数)

# 提交数据
cur.execute('commit')

# 封装成类
class my_sql():
    # 初始化函数 租用：只要调用这个数据库类，就会执行这个init函数
    def __init__(self):
        try:
            self.con = pymysql.connect(host='127.0.0.1', port='2222', user='root', password='admin', database='LIB1')
            # 连接数据库的信息可以存在config文件中
        except Exception as e:
            print(e)
    # 查询
    def select_query(self,sql):
        cur = self.con.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return result

    # 增加、删除、修改
    def insert_query(self,sql):
        try:
            cur = self.con.cursor()
            cur.execute(sql)
            cur.execute('commit')
            return True
        except Exception as e:
            cur.execute('rollback')
            print("添加语句失败"%e)