
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import requests
import pickle
import time
from selenium import webdriver as wbd



with open("data.log_in_id_rp", "rb") as fw:
    id_ = pickle.load(fw)
with open("data.log_in_name_rp", "rb") as pkl:
    id_name = pickle.load(pkl)
with open("data.log_in_id_rp", "wb") as fw:
    pickle.dump(id_, fw)
with open("data.log_in_name_rp", "wb") as pkl:
    pickle.dump(id_name, pkl)
with open("data.history_rp", "rb") as history:
    search_history = pickle.load(history)
with open("data.history_rp", "wb") as history:
    pickle.dump(search_history, history)

current_user = 00


def source_log_in_():

    def log_in():

        account_ask = input("Do you have account? Y / N : ")
        if account_ask == "N" or account_ask == "n":
            print("Making Account...\n")
            account_making()
        elif account_ask == "y" or account_ask == "Y":
            print("Proceeding log in...\n")
            log_in_account()

    def account_making():

        m_name = input("Enter your name")
        m_id = input("Please Enter New ID.")
        m_pw = input("Please Enter New Password.")
        id_[m_id] = m_pw
        id_name[m_id] = m_name
        search_history = []
        with open("data.log_in_id_rp", "wb") as fw:
            pickle.dump(id_, fw)
        with open("data.log_in_name_rp", "wb") as pkl:
            pickle.dump(id_name, pkl)
        with open("data.user_data_rp; %s"%m_id, "wb") as user_data_pickle:
            pickle.dump(search_history, user_data_pickle)

        log_in_account()

    def log_in_account():

        global current_user

        time.sleep(1)
        with open("data.log_in_id_rp", "rb") as fw:
            data = pickle.load(fw)
        with open("data.log_in_name_rp", "rb") as pkl:
            data3 = pickle.load(pkl)
        lg_id = input("Enter Your Id.\n_______________\n")
        while True:
            if lg_id in data:
                while True:
                    lg_pw = input("Enter Your password.\n________________\n")
                    if data[lg_id] == lg_pw:
                        name = data3[lg_id]
                        print("welcome "+name + ".\n________________")

                        break
                    elif id_[lg_id] != lg_pw:
                        print("Check your password.\n")
            else:
                print("Check your ID\n")
                log_in_account()
        
            break
        current_user = lg_id
        
        

    log_in()

log_in_reqest = input("Do you want log_in? : Y / N : ")

if log_in_reqest == "y" or log_in_reqest == "Y":
    print("proceeding log in.")
    time.sleep(0.5)
    source_log_in_()

elif log_in_reqest == "n" or log_in_reqest == "N":
    print("Start with guest account. \n")
    time.sleep(0.5)

if log_in_reqest == "y" or log_in_reqest == "Y":
    with open("data.user_data_rp; %s"%current_user, "rb") as user_data_pickle:
        my_searched_list = pickle.load(user_data_pickle)

    print("your search history.", my_searched_list)

baseurl = "https://www.10000recipe.com/recipe/list.html?q="

print("search with main ingredient : ing")
print("search with name : name\n")
search_type = input("which type you want to wearch with?")

if search_type == "ing":

    addurl = input("Enter main Ingredient of food: ")

    url = baseurl + quote_plus(addurl)

    res = requests.get(url)
    soup = bs(res.text, "html.parser")

    food_name = soup.find_all("div", {"class" : "s_category_tag"})

    food1 = food_name[0].text

    food2 = food1.split('\n')

    rec_final = food2[2:]

    rec_final.pop()
    rec_final.pop()

    rec_final_href = []

    print(rec_final)
    user_finding = str(input("Enter name of food."))

elif search_type == "이름":
    user_finding = str(input("Enter name of food."))
    
if log_in_reqest == "y" or log_in_reqest == "Y":
    with open("data.user_data_rp; %s"%current_user, "rb") as user_data_pickle:
        search_history = pickle.load(user_data_pickle)

    search_history.append(user_finding)


    with open("data.user_data_rp; %s"%current_user, "wb") as user_data_pickle:
        pickle.dump(search_history, user_data_pickle)


user_find = "%s"%user_finding


final_url = "https://www.10000recipe.com/recipe/list.html?q="+user_finding

dv = requests.get(final_url)
soup2 = bs(dv.text, "html.parser")


food_tag = soup2.find_all('a', {"class" :  "common_sp_link"})

for a in food_tag:
    href = a.attrs['href']
    text = a.string


url_final = "https://www.10000recipe.com"+href

dv = requests.get(url_final)
sp= bs(dv.text, "html.parser")


intd = sp. find_all('div', attrs = {'class' : "cont_ingre2"})

ingre = sp.find_all('span', {"class" : "ingre_unit"})

ingred = ingre[0].text

ingre_unit_count = []
for ingre_unit in ingre:
    ingre_unit_count.append(ingre_unit) 

ing = intd[0].text


ing = ing.rstrip()
ing_list = ing.split('\n')
ing_list.remove('재료Ingredients')
ing_list.remove('계량법 안내')


while '' in ing_list:
    ing_list.remove('')




bb = len(ing_list)
b = 1
intt = ('1','2','3','4','5','6','7','8','9','0','약간','조금')
for elements in ing_list:

    if elements != '[재료]':
        if elements.startswith(intt):
            print('  '+elements,"\n______________________________")
        else:
            print(str(b)+'.'+elements,"\n")
            b = b + 1
    
print("\n")
    
        
recipe1 = sp.find_all('div', {"class" : "view_step"})

recipee = recipe1[0].find_all('div', {"class" : "media-body"})
recipe_order = []
a1 = 0
for x in recipee:
    a1 = a1 + 1
    rex = x.text
    recipe_order.append(rex)

for rec_o in recipe_order:
    rec_o.split('\n')

a = 0
for recipe_o in recipe_order:
    a = a+1
    print(str(a)+".",recipe_o,"\n")

check = input("Did you get information you wanted? : Y or N ")

if check == "n" or check == "N":
    dvs = wbd.Chrome("D:\chromedriver.exe")
    dvs.get(final_url)

elif check == "y" or check == "Y":
    print("Thank you for use.")
