from pymongo import MongoClient


class DBMgr:
    def __init__(self):
        # 連結資料庫
        conn = MongoClient('mongodb+srv://b10723052:qGbTI3YJXfCbj9zf@cluster0.np674.mongodb.net'
                           '/Cluster0?retryWrites=true&w=majority')
        db = conn.DB_final
        self.collection = db.vaccine

    def insert(self, item):
        result = self.collection.insert_one(item)
        return result

    def query(self, key, value):
        result = self.collection.find_one({key: value}, {'id': 0})
        return result

    def modify(self, myQuery, newValue):
        result = self.collection.update_one(myQuery, newValue)
        return result

    def delete(self, myQuery):
        result = self.collection.delete_one(myQuery)
        return result
