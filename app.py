import requests
import _testimportmultiple
from requests.structures import CaseInsensitiveDict
from colorama import Fore, Style, init
import os
import time
import json
import sys
config = json.load(open('config.json', 'r'))
token = config['token_tds']
init(convert=True)
os.system("cls")

cookie = input('\033[1;97mVui lòng nhập cookies Ins: ')


def banner():
    banner = f"""
\033[1;97m~ \033[1;92mTool : \033[1;97mTraoDoiSub-Instagram
\033[1;97m~ \033[1;92mAuthor : \033[1;97mNguyen-Tai-Hieu
\033[1;97m~ \033[1;92mSupport : \033[1;97mHacker-No1
\033[1;97m~ \033[1;92mFacebook : \033[1;97mhttps://facebook.com/ke.thong.tri.facebook.2005
\033[1;97m~ \033[1;92mGithub : \033[1;97mhttps://github.com/taihieu2005
\033[1;97m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        time.sleep(0.0000100)


x = 0
os.system('clear')
os.system('cls')
banner()
print('\033[1;97m~ \033[1;92m1 : \033[1;97mFollow')
print('\033[1;97m~ \033[1;92m2 : \033[1;97mLike')
try:
    choose = int(input('Vui lòng chọn: '))
    print(
        '\033[1;97m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
except:
    print('Vui lòng nhập số')
    exit()

if choose == 1:
    getList = config['type']['follow']['get_list']
    cache_type = config['type']['follow']['duyet_nv']
elif choose == 2:
    getList = config['type']['heart']['get_list']
    cache_type = config['type']['heart']['duyet_nv']
else:
    print('Lựa chọn không hợp lệ!')
    exit()


def cookie_to_dict(cookie):
    dic = {}
    cks = cookie.split(';')
    for x in cks:
        chk = x.split('=')
        if len(chk) == 2:
            def lam(x): return x.replace(' ', '')
            dic[lam(chk[0])] = lam(chk[1])
    return dic


def headers(csrf_token):
    headers = CaseInsensitiveDict()
    headers["authority"] = "www.instagram.com"
    headers["accept"] = "*/*"
    headers["accept-language"] = "vi,en;q=0.9,en-US;q=0.8"
    headers["content-type"] = "application/x-www-form-urlencoded"
    headers["origin"] = "https://www.instagram.com"
    headers["referer"] = "https://www.instagram.com/"
    headers["sec-ch-prefers-color-scheme"] = "dark"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
    headers["x-csrftoken"] = csrf_token
    headers["x-requested-with"] = "XMLHttpRequest"
    headers["x-instagram-ajax"] = "1005951515"
    headers["x-requested-with"] = "XMLHttpRequest"
    return headers


def action(id, cookie, type):
    if type == 1:
        urlAction = "https://www.instagram.com/web/friendships/" + id + "/follow/"
    elif type == 2:
        urlAction = "https://www.instagram.com/web/likes/" + id + "/like/"

    url = "https://www.instagram.com/data/shared_data/"
    rq = requests.get(url, cookies=cookie).json()
    csrf_token = rq['config']['csrf_token']
    resp = requests.post(urlAction, headers=headers(
        csrf_token), cookies=cookie)
    try:
        return resp.json()['status'] == 'ok'
    except:
        return False


def getInfoUser(cookie):
    url = "https://www.instagram.com/data/shared_data/"
    rq = requests.get(url, cookies=cookie).json()
    json_data = rq['config']['viewer']
    return json_data['username']


def tds(token, cookie):
    cookies = cookie_to_dict(cookie)
    url = "https://traodoisub.com/api/?fields=profile&access_token=" + token
    resp = requests.get(url).json()
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Tài khoản : {resp['data']['user']}\n{Fore.GREEN}[+]{Style.RESET_ALL} Coins : {resp['data']['xu']}")
    print(
        f"{Fore.GREEN}[+]{Style.RESET_ALL} Đăng nhập thành công tài khoản {getInfoUser(cookies)}")
    while True:
        try:
            listQuest = requests.get(
                f'https://traodoisub.com/api/?fields={getList}&access_token=' + token).json()
            if len(listQuest['data']) == 0:
                print(f"{Fore.RED}[!]{Style.RESET_ALL} Đang tìm nhiệm vụ!")
            else:
                id = listQuest['data'][0]['id']
                link = listQuest['data'][0]['link']
                id_Split = listQuest['data'][0]['id'].split('_')[0]
                followUser = action(id_Split, cookies, choose)
                if followUser:
                    sendQuest = requests.get(
                        f"https://traodoisub.com/api/coin/?type={cache_type}&id=" + id + "&access_token=" + token).json()
                    print(
                        f"{Fore.GREEN}[ TTK ]{Style.RESET_ALL}: {link} | {sendQuest['data']['msg']}$ | {sendQuest['data']['pending']}$ | {sendQuest['data']['cache']}")
                    for i in range(5, -1, -1):
                        print(
                            f'\033[1;31m[\033[0;36m|\033[1;31m] \033[0;97mVui Lòng Đợi {i} •   ', end='\r')
                        time.sleep(0.25)
                        print(
                            f'\033[1;31m[\033[0;36m/\033[1;31m] \033[0;97mVui Lòng Đợi {i} ••    ', end='\r')
                        time.sleep(0.25)
                        print(
                            f'\033[1;31m[\033[0;36m-\033[1;31m] \033[0;97mVui Lòng Đợi {i} •••   ', end='\r')
                        time.sleep(0.25)
                        print(
                            f'\033[1;31m[\033[0;36m\\\033[1;31m] \033[0;97mVui Lòng Đợi {i} ••••    ', end='\r')
                        time.sleep(0.25)
                else:
                    print(
                        f"{Fore.RED}[-]{Style.RESET_ALL} Không thể thực hiện id này!")
        except Exception as e:
            continue


tds(token, cookie)
