print("""
******************
Kullanıcı girişi

******************

""")


sys_kullanıcı_adi = "ppp"
sys_parola = "ppp"

kullanıcıadı = input("Kullanıcı adını giriniz = ")
parola = input("Şifreyi giriniz =")

if (kullanıcıadı== sys_kullanıcı_adi and parola!=sys_parola):
    print("Hatalı parola...")
elif (kullanıcıadı!=sys_kullanıcı_adi and parola==sys_parola):
    print("Hatalı kullanıcı adı...")
elif (kullanıcıadı!=sys_kullanıcı_adi and parola!=parola):
    print("Kullanıcı adı ve parola hatalı...")
else:
    print("Başarılı giriş")





