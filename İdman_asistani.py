#MARATON İDMAN ASİSTANI
import math 

#Bu fonksiyonu dakıka ve sanıye cınsınden verilen sureyı sadece saniyeye cevirir

def toplam_saniye(dk, sn):
    return dk * 60 + sn

#Bu fonksiyon 1 mil kosmak ıcın gereklı sureyı mıl/saat cınsınden hıza cevırır
def hız(time):
    return 3600 / time

#Kullanıcıdan bir mil için gereklı sureyı ve mesafeyı al 
sure_dk = int(input ('1 mil icin gereklı dakıka? '))
sure_sn = int(input('1 mil icin gereklı sanıye? '))
mesafe = int(input('Toplam mesafe? '))

#Hızı hesapla ve yaz
mph = hız(toplam_saniye(sure_dk, sure_sn))
print('Hızınız')
print(mph)

#İdman suresini hesapla
total = mesafe * toplam_saniye(sure_dk, sure_sn)
gecen_dakika = ('toplam // 60')
gecen_saniye = ('toplam % 60') 

print('Toplam gecen sure')
print(gecen_dakika)
print(gecen_saniye)







