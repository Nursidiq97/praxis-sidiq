print("Selamat Datang Di ATM Saya")
print("Pilih Option :")
print("1. Check Uang Saya")
print("2. Ambil Uang Saya")
print("3. Tabung Saya")
option=int(input("Silahkan Pilih Option :"))
if (option==1): 
    print("Uang Kamu Berjumlah Rp.500.000")
elif (option==2):
    print("Uang Kamu Berjumlah Rp.500.000, Mau Ambil Berapa")
    print("1. Rp.100.000")
    print("2. Rp.200.000")
    uang_kamu=500.000
    option2=int(input("option :"))
    if option2==1:
        hasil=uang_kamu-100.0000
        print("Uang Kamu Sekarang Berjumlah :",hasil)
    elif option2==2:
        hasil=uang_kamu-500.0000
        print("Uang Kamu Sekarang Berjumlah :",hasil2)
    else:
        print("Keyword Anda Salah!")
elif option==3:
    uang_kamu=500.000
    print("Uang Kamu Berjumlah Rp.500.000, Mau Nabung Berapa?")
    option3=int(input("Masukan Jumlah Uang :"))
    hasil3=uang_+option3
    print("Jumlah Uang Kamu Sekarang Adalah ", hasil3)
else:
    print("Keyword Anda Salah Mohon Coba Lagi!")


        


