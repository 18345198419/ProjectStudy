import requests
import re
import time

s = requests.session()


class TaobaoLogin:
    def __init__(self, ua, account, TPL_password2):
        self.account = account  # 淘宝用户名
        self.ua = ua  # 淘宝关键参数，包含用户浏览器等一些信息，很多地方会使用，从浏览器或抓包工具中复制，可重复使用
        self.TPL_password2 = TPL_password2  # 加密后的密码，从浏览器或抓包工具中复制，可重复使用

    def user_check(self):
        print("1.调用账户是否需要滑动验证码接口(True:需要/False:不需要)")
        user_check_url = "https://login.taobao.com/member/request_nick_check.do?_input_charset=utf-8"
        data = {
            "username": self.account,
            "ua": self.ua
        }
        try:
            user_check_response = s.post(user_check_url, data=data)
        except Exception as e:
            print("用户验证接口请求失败，msg:")
            raise e

        user_check_result = user_check_response.json()["needcode"]
        print("2.返回结果为:%s" % user_check_result)
        if not user_check_result:
            pass
        else:
            print("3.需要滑动验证，搞不定！休息10秒再来一次试试")
            time.sleep(10)
            self.user_check()

        return user_check_result

    def get_token(self):
        if not self.user_check():
            print("3.调用验证密码获取token的接口")
            verify_password_url = "https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F"
            verify_password_headers = {
                "Connection": "keep-alive",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://login.taobao.com",
                "referer": "https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
            }
            verify_password_data = {
                "TPL_username": self.account,
                "TPL_password": "",
                "TPL_password_2": self.TPL_password2,
                "ncoSig": "",
                "ncoSessionid": "",
                "ncoToken": "6617f9d84e25f8f774ad1b5d6a7fa5336c5fe3b2",
                "slideCodeShow": "false",
                "useMobile": "false",
                "lang": "zh_CN",
                "loginsite": "0",
                "newlogin": "0",
                "TPL_redirect_url": "https://www.taobao.com/",
                "from": "tb",
                "fc": "default",
                "style": "default",
                "css_style": "",
                "keyLogin": "false",
                "qrLogin": "true",
                "newMini": "false",
                "newMini2": "false",
                "tid": "",
                "loginType": "3",
                "minititle": "",
                "minipara": "",
                "pstrong": "",
                "sign": "",
                "need_sign": "",
                "isIgnore": "",
                "full_redirect": "",
                "sub_jump": "",
                "popid": "",
                "callback": "",
                "guf": "",
                "not_duplite_str": "",
                "need_user_id": "",
                "poy": "",
                "gvfdcname": "10",
                "gvfdcre": "8747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D613231626F2E323031372E3735343839343433372E372E356166393131643959427031513326663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246",
                "from_encoding": "",
                "sub": "",
                "loginASR": "1",
                "loginASRSuc": "1",
                "allp": "",
                "oslanguage": "zh-CN",
                "sr": " 1920*1080",
                "osVer": "",
                "naviVer": "chrome|74.03729131",
                "osACN": "Mozilla",
                "osAV": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                "osPF": "Win32",
                "miserHardInfo": "",
                "appkey": "00000000",
                "nickLoginLink": "",
                "mobileLoginLink": "https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true",
                "showAssistantLink": "",
                "um_token": " TF4565FB51ACF66D3CFA13717D3CAC2903A6C266FC2AF9490AEC8FDD715"
            }

            verify_password_res = s.post(verify_password_url, headers=verify_password_headers, data=verify_password_data)
            # print(res.text)

            st_token_url = re.search(r'', verify_password_res.text).group(1)
            print("4.获取到st_token_url:" + st_token_url)
            print("5.get请求st_token_url，以获取token")
            st_response = s.get(st_token_url)
            st_token = re.search(r'data":{"st":"(.*?)"}}', st_response.text).group(1)
            print("6.st_token:" + st_token)
            return st_token

    def get_nick_name(self):
        my_taobao_url = 'https://login.taobao.com/member/vst.htm?st='+self.get_token()
        my_taobao_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        taobao_response = s.get(my_taobao_url, headers=my_taobao_headers)
        # print(taobao_response.text)
        my_taobao_match = re.search(r'top.location.href = "(.*?)";', taobao_response.text).group(1)
        # print("taobao_location:"+str(my_taobao_match))
        print("7.跳转到我的淘宝链接:"+my_taobao_match)

        res = s.get(my_taobao_match,headers=my_taobao_headers)
        # print(res.text)
        nick_name_match = re.search(r'', res.text).group(1)
        print("8.我的淘宝昵称是:"+nick_name_match)


if __name__ == '__main__':
    ua = "119#MlNFNUnqMmAQXMMzpRq2fkNz/uKyPFnURt9HyBGj7YZ9//Wd1kKDT4rW4f5hui3dBZzz1z2P1SoYAY"\
         "akpxyOJOnY3CIF9U+S4lkGIrAtk2RVNMkGqEAsy7KpztNLE1Tl4l9L3eALR2BVNEjy9eAzRzsnfWkmGovzw"\
         "lv4IrYLRJKVxzMQfe3F7PSe3AA89UXq4l9GdwtFyw/VfzzRFX6SO/JTg6pQM6ILfP5h5K7HnTjHjp5m6tgl"\
         "mQVmEdWOGMENQZFTa/ByxWroJPDnAwAknxX3ZXsfUaPUTxlLoXGDqYryjiAQXaVrHv//kpxNj+zGSHozFkO"\
         "i08n1tesrkdmwYF4oxpJGqk0HXr08jx4AIGXzTHIAUjYD+9zRZXdxS8UkGhRrgw3Gml0errEb7cB6/dQz3R5"\
         "Qj2fQ47uEke4FzQeZlsL5Gug/s+5C+w8wo8UGgX01WVOule9loCO5TfCEPyaHn6WJI3TovNfShG0lgkV/CgBK"\
         "qGE+guT/Q2M3xcUqwjjpIbr3nWde2DPbtsPf6e25eurzZklClT7tn8PWGjiANHGlI0RsUWzTcYruIrCCa975"\
         "Wm/Hh1MsjX0iF+dP/xBr+1X2p23Jnz81UxfAcn3zi8ojxR9cf/C8I0X/lu9xlo7VO8FGXb1KfveZlUPJ23Yp"\
         "xvhOrlCGoTcGEUdJq8BQGyw5Pyp4SVxEZhi97UvLoekSRpyc5fDeTN4GM6PordX4lLYYYvAHkveLNYgbV2bj"\
         "YVSdX3GUqcAKEDQ7xBpRZ6JiTHWY7Y9hfG5NAjyft/RiGU9R+rpsDC8iXmWoacx4pHoFf+bExj9HHDLelhN2"\
         "Gs+m9q+tQcLYknsfFLDYHjdT90yszHBCWJnT26yPrG8TBu0bPkzzldwYvC=="
    TPL_password2 = "660e8305092ec04ec1e99e374a4a246742fdb1cac45d78bfce35ef98bdc24a04794eba1d40a604f82efb8fcc4e28d85b0e2c12f2535f10fedc8a95f7739a6a99d0e2b96cdbaae3f42e903d6439561b3f4c3419c40eb191b2ada1179e1f874cf70e0109041d249ef27d2882b72f0f33020888b162023ee408be2a105e15c62dbf"
    account = "淘宝账号"
    login = TaobaoLogin(ua=ua,account=account,TPL_password2=TPL_password2)
    login.get_nick_name()