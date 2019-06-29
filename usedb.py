import meradb
db = meradb.load("table.db")
db.set('sonam ','kumawat')
db.set('shivam ','shukla')

db.get('key')
db.get_all()
# db.rem('key')
# db.exists('key')
# db.total_keys()
# db.del_db('key')
db.dump()