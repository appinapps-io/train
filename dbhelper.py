import sqlite3
from datetime import date
import json


DB_PATH = './db_todo.db'
today = date.today()
time = date.today()

#conn = sqlite3.connect(DB_PATH)
#c = conn.cursor()
#c.execute()
#conn.commit()

def get_all_items():
	try:
		conn = sqlite3.connect(DB_PATH)
		c = conn.cursor()
		c.execute("select * from items")
		rows = c.fetchall()
		print(rows)
		j = make_dicts(rows)
		return j
	except Exception as e:
		print('Error : ' , e)
		return None

def add_to_list(title):
		try:
			conn = sqlite3.connect(DB_PATH)
			c = conn.cursor()
			c.execute("insert into items(title,status,date,time) values(?,?,?,?)",(title,'Not Started',today.strftime("%Y:%m:%d"),today.strftime("%H:%M:%S")))       
			conn.commit()
			return {"title":title}
		except Exception as e:
			print('Error : ' + e)
			return None

def update_item(item):
		try:
			conn = sqlite3.connect(DB_PATH)
			c = conn.cursor()
			c.execute("update items set title=?,status=? where id=?",(item['title'],item['status'],item['id']))       
			conn.commit()
			return {"id":item['id']}
		except Exception as e:
			print('Error : ' + e)
			return None

def delete_item(id):
		try:
			conn = sqlite3.connect(DB_PATH)
			c = conn.cursor()
			c.execute("delete from items where id=?",(id,))       
			conn.commit()
			return {'id':id}
		except Exception as e:
			print('Error : ' + e)
			return None


def make_dicts(rows):
    objects_list = []
    for row in rows:
        d = {}
        d['id'] = row[0]
        d['title'] = row[1]
        d['status'] = row[2]
        d['date'] = row[3]
        d['time'] = row[4]
        objects_list.append(d)
    j = json.dumps(objects_list)
    return j