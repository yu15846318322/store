import xlrd
import pymysql

wd =xlrd.open_workbook(filename=r"2020年每个月的销售情况.xlsx",encoding_override=True)

db = pymysql.connect(host="localhost",user='root',password='root',database='2020销售数据库')
cursor = db.cursor()
sql = "insert into day values(%s,%s,%s,%s,%s)"
for i in range(1,13):

    st = wd.sheet_by_name("%s月"%(i))
    cols = st.ncols
    rows = st. nrows
    for row in range(1, rows):
        data = st.row_values(row)
        param = ["%s月"%(i)+data[0], data[1], data[2], data[3], data[4]]
        cursor.execute(sql, param)
db.commit()
cursor.close()
db.close()