import requests
import json
from ast import literal_eval
# dbd_dictionary_similar

class CRUD():
    def __init__(self):
        # database test
        self.name_database = 'test_similar'
        # database จริง
        # self.name_database = 'dbd_dictionary_similar'
# เดียวเเก้ { "result": []}
    def read_all(self):
        url = f"http://10.10.14.212:9200/{self.name_database}/_search"   
        payload='{"query":{"bool":{"must":[{"match_all":{}}],"must_not":[],"should":[]}},"from":0,"size":10000,"sort":[],"aggs":{}}'
        headers = {'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers, data=payload)
        r_json = response.json()['hits']['hits']
        return r_json, True

    def read_each(self, search_id):
        all_data = self.read_all()[0]
        for i in range(len(all_data)):
            if str(search_id) == str(all_data[i]['_id']):
                return all_data[i]['_source'], True
        return 'not find id in database', False

    def create_es(self,search_id,dict_data):
        old_data = self.read_each(search_id)[0]
        url = f"http://10.10.14.212:9200/{self.name_database}/my_type/{search_id}"
        payload = json.dumps(dict_data)
        headers = {'Content-Type': 'application/json'}
        # update
        if old_data != 'not find id in database':
            response = requests.request("POST", url, headers=headers, data=payload)
            return dict_data, 'update_success', True
        # create
        else:
            response = requests.request("POST", url, headers=headers, data=payload)
            return dict_data, 'create_success', True
    def delete_es(self,search_id):
        old_data = self.read_each(search_id)[0]
        if old_data == 'not find id in database':
            return old_data, 'not find id in database', False
        else:
            url = f"http://10.10.14.212:9200/{self.name_database}/my_type/{search_id}"
            payload={}
            headers = {}
            response = requests.request("DELETE", url, headers=headers, data=payload)
            return old_data, 'delete success', True

# a = CRUD().read_all()
# read_each
# a = CRUD().read_each(3)
# create and update
# a = CRUD().create_es(7,{"list_soundex": ["test12"],"list_word": ["test2"],"unique_column": "cc00036"})
# delete
# a = CRUD().delete_es(6)
# print(a)



    # def read_each(self,search_unique):
    #     url = f"http://10.10.14.212:9200/{self.name_database}/_search"
    #     payload='{"query":{"bool":{"must":[{"match":{"unique_column.keyword":"%s"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}'%(search_unique)
    #     headers = {'Content-Type': 'application/json'}
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     r_json = response.json()['hits']['hits']
    #     list_id = []
    #     list_word = []
    #     list_soundex = []
    #     list_unique = []
    #     for i in range(len(r_json)):
    #         list_id.append(r_json[i]['_id'])
    #         list_word.append(r_json[i]['_source']['list_word'])
    #         list_soundex.append(r_json[i]['_source']['list_soundex'])
    #         list_unique.append(r_json[i]['_source']['unique_column'])
    #     return list_id,list_word,list_soundex,list_unique

    # def create_es(self, add_list_word, add_list_soundex, add_unique_column):
    #     check_data = self.read_each(add_unique_column)[3]
    #     # literal_eval('[1.23, 2.34]')
    #     if len(check_data) == 0:
    #         dict_data = {
    #             "list_word": literal_eval(add_list_word),
    #             "list_soundex": literal_eval(add_list_soundex),
    #             "unique_column": add_unique_column
    #         }
    #         url = f"http://10.10.14.212:9200/{self.name_database}/my_type/"
    #         payload = json.dumps(dict_data)
    #         headers = {'Content-Type': 'application/json'}
    #         response = requests.request("POST", url, headers=headers, data=payload)
    #         print('create_success',dict_data)
    #         return dict_data
    #     else:
    #         return 'it is duplicate unique column'


    # def update_es(self, update_list_word, update_list_soundex, update_unique_column):
    #     check_unique = self.read_each(update_unique_column)[3]
    #     check_id = self.read_each(update_unique_column)[0][0]
    #     if len(check_unique) != 0:
    #         dict_data = {
    #             "list_word":update_list_word,
    #             "list_soundex":update_list_soundex,
    #             "unique_column":update_unique_column
    #         }
    #         url = f"http://10.10.14.212:9200/{self.name_database}/my_type/{check_id}"
    #         payload = json.dumps(dict_data)
    #         headers = {'Content-Type': 'application/json'}
    #         response = requests.request("POST", url, headers=headers, data=payload)
    #         return 'update success'
    #     else:
    #         return 'not unique in database'


    # def delete_es(self,delete_unique_column):
    #     check_unique = self.read_each(delete_unique_column)[3]
    #     if len(check_unique) != 0:
    #         check_id = self.read_each(delete_unique_column)[0][0]

    #         url = f"http://10.10.14.212:9200/{self.name_database}/my_type/{check_id}"
    #         payload = {}
    #         headers= {}
    #         response = requests.request("DELETE", url, headers=headers, data = payload)
    #         # print(response.json())
    #         return 'delete success'
    #     else:
    #         return 'not unique in database'


# test = CRUD().read_all()
# test = CRUD().read_each('cc00027')
# test = CRUD().create_es(['ทราย', 'ซายน์', 'ซาย', 'ไซน์'],[['ท9700'], ['ซ9000ย0000'], ['ซ9000ย0000'], ['ซ7000']],'cc00027')
# test = CRUD().update_es(['test'],[['test']],'cc00027')
# test = CRUD().delete_es('cc00027')
# {
#     "list_soundex": [
#         "test"
#     ],
#     "list_word": [
#         "test"
#     ],
#     "unique_column": "cc00033"
# }

