import pickle

id_ = {}
id_name = {}

user_finded_recipe = {}

with open("data.log_in_id_rp", "wb") as fw:
    pickle.dump(id_, fw)
with open("data.log_in_name_rp", "wb") as pkl:
    pickle.dump(id_name, pkl)
with open("data.history_rp", "wb") as history:
    pickle.dump(user_finded_recipe, history)
