![100px-MIT_logo shields](https://img.shields.io/github/license/talhatugsat1/yemeksepeti-account-checker) ![100px-MIT_logo shields](https://img.shields.io/github/stars/talhatugsat1/yemeksepeti-account-checker?style=social)
# yemeksepeti-account-checker
Yemeksepeti hesaplarınızın geçerli olup olmadığını kontrol eder.

## Örnek Kullanım

```python
checker = YemeksepetiChecker() # classı çağırıyoruz
checker.setCountry("hatay") # işlemin yapılıcağı şehiri belirliyoruz
print(checker.setProxy("8.8.8.8", "80", "http")) # eğer ihtiyacınız varsa proxyi belirliyoruz
token = checker.getToken() # güvenlik tokenini alıyoruz
checker.setAccount("gmail@gmail.com", "youultrasecretpass") # hesabın mail adresini ve şifresini giriyoruz
print(checker.check(token)) # sorguyu gönderiyoruz, eğer hesap aktifse olumlu (true) değeri geri dönecektir. Aksi halinde olumsuz (false) değeri döner.

```

## MIT License
[![220px-MIT_logo svg](https://user-images.githubusercontent.com/51381316/134710284-22a012b1-fe1b-4b01-8f4c-62d02d261718.png)](https://github.com/talhatugsat1/yemeksepeti-account-checker/blob/main/LICENSE)

## Contact
[![Linkedin](https://img.shields.io/badge/talhatugsat-follow%20on%20linkedin-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/talha-tu%C4%9Fsat-88303a1b0/) [![R10](https://img.shields.io/badge/leaver-view%20on%20r10.net-blue?style=for-the-badge)](https://www.r10.net/profil/133573-leaver.html)

## Stats
<p float="center">
  <img  src="https://github-readme-stats.vercel.app/api?username=talhatugsat1&show_icons=true&count_private=true&hide=contribs,issues" alt="talhatugsat1's github stats" />
</p>
