import csv

file = open('users.csv', 'r')
r = file.read().split("\n")
harfler= {
    "ı" : "i",
    "ç" : "c",
    "ş" : "s",
    "ğ" : "g",
    "ö" : "o",
    "ü" : "u"
}

def convert(metin):
    for i in harfler:
        if i in metin:
            metin=metin.replace(i, harfler[i])
    return metin



users={}

fieldnames = ['Ad', 'Soyadı', 'E-posta Adresi', 'Şifre', 'Kuruluş Birimi Yolu']


with open("usernamePass.csv", mode="w") as userlar:
    # uw = csv.writer(userlar, delimiter=";", quotechar='"')
    uw = csv.DictWriter(userlar, fieldnames=fieldnames)
    for i in r:
        uw.writerow({'Ad': i.split(";")[0].strip(),
                     'Soyadı': i.split(";")[1].strip(),
                     'E-posta Adresi': convert(i.split(";")[0].split(" ")[0]).lower()+"."+convert(i.split(";")[1]).lower()+"@alfagrup.k12.tr",
                     'Şifre': i.split(";")[2][:6]+".Alfa2013",
                     'Kuruluş Birimi Yolu':"/"})
# First Name,Last Name,Email Address,Password,Org Unit Path


