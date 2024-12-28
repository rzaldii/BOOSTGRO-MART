import csv
import os
import pandas as pd

#====================================================================================================================
# BUAT NGE CLEAR
#====================================================================================================================
def clear():
    os.system('cls')
    judul(">>>>>   B O O S T G R O  M A R T   <<<<<","harga murah, transaksi mudah, kualitas mewah")


#====================================================================================================================
# HEADER ATAU JUDUL APLIKASI dan JUDUL HALAMAN
#====================================================================================================================
lebar = 96

def judul(nama, slogan):
    print(f"|{"="*lebar}|")
    print(f"|{nama.center(lebar)}|")
    print(f"|{("( "+slogan+" )").center(lebar)}|")
    print(f"|{"="*lebar}|")

def judul_halaman(nama,):
    print(f"|{nama.center(lebar)}|")
    print(f"|{"="*lebar}|")


#====================================================================================================================
# FUNGSI EXIT (keluar)
#====================================================================================================================
def exit():
    os.system('cls')
    print(f"|{"="*lebar}|")
    judul_halaman("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI :)")
    pilihan = input("\nIngin menggunakan program kami lagi? [y/n] : ")
    if pilihan == "y":
        tampilan_awal()


#====================================================================================================================
# FUNGSI TABEL MENU
#====================================================================================================================
daftar_tampilan_awal = ["1. Admin","2. Customer", "Out (o)"]
back_out = ["Back (b)", "Out (o)"]

mode_admin = ["1. Login", "Back (b)","Out (o)"]
daftar_menu_admin = ["1. Manage Produk", "2. Manage Jasa Pengiriman", "3. Rekap Penjualan"]
menu_manage_produk = ["1. Tampilkan Produk", "2. Tambah Produk", "3. Ubah Produk", "4. Hapus Produk"]
menu_manage_pengiriman1 = ["1. Tampilkan Jasa Pengiriman", "2. Tambah Jasa Pengiriman"]
menu_manage_pengiriman2 = ["3. Ubah Jasa Pengiriman", "4. Hapus Jasa Pengiriman"]

mode_customer = ["1. Login", "2. Register", "Back (b)","Out (o)"]
daftar_menu_customer = ["1. Lihat Daftar Produk", "2. Pesan/Beli Produk"]

def tabel_menu(nama_menu):
    lebar_menu = lebar//len(nama_menu)
    for i in range(len(nama_menu)):
        if i == len(nama_menu) - 1:
            print("|"+nama_menu[i].center(lebar_menu)+"|",end="")
        else:
            print("|"+nama_menu[i].center(lebar_menu-1),end="")

    print(f"\n|{"="*lebar}|")


#====================================================================================================================
# TAMPILAN AWAL
#====================================================================================================================
def tampilan_awal():
    clear()
    tabel_menu(daftar_tampilan_awal)
    pilihan = input("\nPilih : ")
    
    while pilihan != "1" and pilihan != "2" and pilihan != "o":
        clear()
        tabel_menu(daftar_tampilan_awal)
        print("\nPilih menu yang tersedia !!!")
        pilihan = input("Pilih : ")
    
    if pilihan == "1":
        admin()

    if pilihan == "2":
        customer()

    if pilihan == "o":
        exit()


#====================================================================================================================
# TAMPILAN AWAL ADMIN
#====================================================================================================================
def admin():
    clear()
    judul_halaman("H A L A M A N  A D M I N")
    tabel_menu(mode_admin)
    pilihan = input("\nPilih : ")

    while pilihan != "1" and pilihan != "b" and pilihan != "o":
        clear()
        judul_halaman("H A L A M A N  A D M I N")
        tabel_menu(mode_admin)
        print("\nPilih menu yang tersedia !!!")
        pilihan = input("Pilih : ")

    if pilihan == "1":
        login_admin()

    elif pilihan == "b":
        tampilan_awal()

    elif pilihan == "o":
        exit()


#====================================================================================================================
# TAMPILAN AWAL CUSTOMER
#====================================================================================================================
def customer():
    clear()
    judul_halaman("H A L A M A N  C U S T O M E R")
    tabel_menu(mode_customer)
    pilihan = input("\nPilih : ")

    while pilihan != "1" and pilihan != "2" and pilihan != "b" and pilihan != "o": 
        clear()
        judul_halaman("H A L A M A N  C U S T O M E R")
        tabel_menu(mode_customer)
        print("\nPilih menu yang tersedia !!!")
        pilihan = input("Pilih : ")

    if pilihan == "1":
        login_customer()

    elif pilihan == "2":
        register()

    elif pilihan == "b":
        tampilan_awal()
            
    elif pilihan == "o":
        exit()


#====================================================================================================================
# FUNGSI LOGIN
#====================================================================================================================
def login_admin():
    clear()
    judul_halaman("H A L A M A N  L O G I N  A D M I N")

    data_akun = []
    valid = False
    kesempatan_salah = 3

    while valid == False:
        username = input("\nMasukkan username : ")
        password = input("Masukkan password : ")
        
        with open("akun_admin.csv", "r") as data:
            lihat_data = csv.DictReader(data)
            for akun_admin in lihat_data:
                data_akun.append(akun_admin)

            for row in data_akun:
                if username != row["username"] or password != row["password"]:
                    continue
                elif username == row["username"] and password == row["password"]:
                    valid = True
                    if valid == True:
                        clear()
                        judul_halaman("H A L A M A N  L O G I N  A D M I N")
                        print("\nBERHASIL LOGIN !!!")
                        input("\nKlik [ENTER] untuk melanjutkan.")
                        menu_admin()
                        break

            else:
                clear()
                judul_halaman("H A L A M A N  L O G I N  A D M I N")
                print("\nUsername atau password salah !!!")
                kesempatan_salah -= 1
            
        if kesempatan_salah == 0:
            valid = True
            if valid == True:
                input("\nKesempatan sudah habis, klik [ENTER] untuk kembali.")
                admin()
                break


def login_customer():
    clear()
    judul_halaman("H A L A M A N  L O G I N  C U S T O M E R")

    data_akun = []
    valid = False
    kesempatan_salah = 3

    while valid == False:
        global username
        username = input("\nMasukkan username : ") 
        password = input("Masukkan password : ")
        
        with open("akun_customer.csv", "r") as data:
            lihat_data = csv.DictReader(data)
            for akun_customer in lihat_data:
                data_akun.append(akun_customer)
            
            for row in data_akun:
                if username != row['username'] or password != row['password']:
                    continue
                elif username == row['username'] and password == row['password']:
                    valid = True
                    if valid == True:
                        clear()
                        judul_halaman("H A L A M A N  L O G I N  C U S T O M E R")
                        print("\nBERHASIL LOGIN !!!")
                        input("\nKlik [ENTER] untuk melanjutkan.")
                        menu_customer()
                        break

            else:
                clear()
                judul_halaman("H A L A M A N  L O G I N  C U S T O M E R")
                print("\nUsername atau password salah !!!")
                kesempatan_salah -= 1

        if kesempatan_salah == 0:
            valid = True
            if valid == True:
                input("\nKesempatan sudah habis, klik [ENTER] untuk kembali.")
                customer()
                break


#====================================================================================================================
# FUNGSI REGISTER
#====================================================================================================================
def register():
    clear()
    judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")

    # data ketentuan username dan password
    minim_karakter_un = 5
    angka = "1234567890"
    list_angka = list(angka)
    simbol = "`~!@#$%^&*-_=+;:',<.>/?"
    list_simbol = list(simbol)
    minim_karakter_pw = 8
    ketentuan_password = f'''Silahkan membuat password dengan ketentuan : 
 1. Minimal {minim_karakter_pw} karakter
 2. Mengandung simbol / karakter khusus ({simbol})
 3. Mengandung angka'''
    
    data_akun = []

    # username
    while True:
        username = input(f"\nMasukkan username : ")
    
        with open("akun_customer.csv", "r") as data:
            lihat_data = csv.DictReader(data)
            for akun_customer in lihat_data:
                data_akun.append(akun_customer)

            ada_spasi = 0
            for karakter in username:
                if karakter == " ":
                    ada_spasi += 1
                    break
                else:
                    continue

            if ada_spasi > 0:
                clear()
                judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")
                print(f"\nUsername tidak boleh mengandung spasi !!!")
            
            elif len(username) < minim_karakter_un: # jika pw kurang dari 5 karakter, maka akan terus di loop
                clear()
                judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")
                print(f"\nUsername minimal harus {minim_karakter_un} karakter !!!")

            akun_tersedia = 0
            for row in data_akun:
                if username == row["username"]:
                    akun_tersedia += 1
                    clear()
                    judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")
                    print("\nUsername telah tersedia, silahkan buat username lain !!!")

            if akun_tersedia == 0 and len(username) >= minim_karakter_un and ada_spasi == 0:                
                valid_username = username
                clear()
                judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")
                print(f"\nUsername = {username}")
                print(f"\n{ketentuan_password}")
                break

    # password
    while True:
        password = input("Masukkan password : ")

        ada_simbol = 0
        ada_angka = 0

        for karakter in password:
            if karakter in list_angka and karakter in list_simbol:
                ada_simbol += 1
                ada_angka += 1
            elif karakter in list_simbol:
                ada_simbol += 1
            elif karakter in list_angka:
                ada_angka += 1

        if len(password) >= minim_karakter_pw and ada_simbol > 0 and ada_angka > 0:
            clear()
            judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")
            print(f"\nUsername = {username}")
            print(f"Password = {password}")            
            valid_password = password
            break

        elif len(password) < 8 or ada_simbol == 0 or ada_angka == 0:
            clear()
            judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")
            print(f"\nUsername = {username}")
            print(f"\n{ketentuan_password}")
            print("\nPassword belum memenuhi ketentuan !!!")

    # nomor telepon
    while True:
        telepon = (input("\nMasukkan nomor telepon : "))
        
        if not telepon.isdigit():
            clear()
            judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")
            print(f"\nUsername = {username}")
            print(f"Password = {password}")
            print("\nNomor telepon harus berupa angka !!!")

        elif len(telepon) < 10 or len(telepon) > 13:
            clear()
            judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")
            print(f"\nUsername = {username}")
            print(f"Password = {password}")
            print("\nNomor telepon harus 10 sampai 13 digit !!!")

        else:
            valid_telepon = telepon
            data_akun_customer = {"username" : valid_username, "password" : valid_password, "nomor telepon" : valid_telepon}
            with open("akun_customer.csv", "a", newline="") as data:
                header = ["username", "password", "nomor telepon"]
                tambah_data = csv.DictWriter(data, fieldnames=header)
                if data.tell() == 0:
                    tambah_data.writeheader()
                tambah_data.writerow(data_akun_customer)

            clear()
            judul_halaman("H A L A M A N  R E G I S T E R  C U S T O M E R")
            print(f"\nUsername\t = {username}")
            print(f"Password\t = {password}") 
            print(f"No.Telepon\t = {telepon}")
            print("\nBERHASIL MEMBUAT AKUN !!!")
            input("\nSilahkan login terlebih dahulu, klik [ENTER]")
            customer()
            break


#====================================================================================================================
# MENU ADMIN
#====================================================================================================================
def menu_admin():
    clear()
    judul_halaman("M E N U  A D M I N")
    tabel_menu(daftar_menu_admin)
    tabel_menu(back_out)
    pilihan = input("\nPilih : ")
    
    while pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "b" and pilihan != "o":
        clear()
        tabel_menu(daftar_menu_admin)
        tabel_menu(back_out)
        print("\nPilih menu yang tersedia !!!")
        pilihan = input("Pilih : ")

    if pilihan == "1":
        manage_produk()

    elif pilihan == "2":
        manage_pengiriman()

    elif pilihan == "3":
        rekap_penjualan()

    elif pilihan == "b":
        admin()
            
    elif pilihan == "o":
        exit()


#====================================================================================================================
# DATA MENU ADMIN
#====================================================================================================================
# Nama file CSV untuk masing-masing kategori
filename_produk = 'daftar_produk.csv'
filename_pengiriman = 'daftar_pengiriman.csv'
filename_transaksi = "data_transaksi.csv"

# Fungsi untuk memastikan file CSV ada
def create_csv_if_not_exists(filename, columns):
    if not os.path.isfile(filename):
        df = pd.DataFrame(columns=columns)
        df.to_csv(filename, index=False)

# Membuat file CSV jika belum ada
create_csv_if_not_exists(filename_produk, ['Nama Produk', 'Harga (Rp)', 'Stok (kg)'])
create_csv_if_not_exists(filename_pengiriman, ['Nama Jasa', 'Biaya'])


#====================================================================================================================
# FUNGSI MANAGE PRODUK
#====================================================================================================================
def tampilkan_produk():
    daftar_produk = []
    with open("daftar_produk.csv", "r") as file:
        lihat_data = csv.DictReader(file)
        for row in lihat_data:
            daftar_produk.append(row)

    judul_halaman("D A F T A R  P R O D U K")
    print(f"| No. |{"Nama Produk".center(40)}|{"Harga (Rp)".center(24)}|{"Stok (kg)".center(24)}|")
    print(f"|{"="*lebar}|")
    for i in range(len(daftar_produk)):
        if i >= 9:
            print(f"| {i+1}. |{daftar_produk[i]["Nama Produk"].center(40)}|{daftar_produk[i]["Harga (Rp)"].center(24)}|{daftar_produk[i]["Stok (kg)"].center(24)}|")
        else:
            print(f"| {i+1}.  |{daftar_produk[i]["Nama Produk"].center(40)}|{daftar_produk[i]["Harga (Rp)"].center(24)}|{daftar_produk[i]["Stok (kg)"].center(24)}|")
    print(f"|{"="*lebar}|")


def tambah_produk(nama_produk, harga, stok):
    df = pd.read_csv(filename_produk)
    new_produk = pd.DataFrame({'Nama Produk': [nama_produk], 'Harga (Rp)': [harga], 'Stok (kg)': [stok]})
    df = pd.concat([df, new_produk], ignore_index=True)
    df.to_csv(filename_produk, index=False)

    print(f"\nProduk '{nama_produk}' berhasil ditambahkan.")
    input("\nKlik [ENTER] untuk kembali.")
    manage_produk() 


def ubah_produk(nama_produk, harga=None, stok=None):
    df = pd.read_csv(filename_produk)
    if nama_produk in df['Nama Produk'].values:
        if harga is not None:
            df.loc[df['Nama Produk'] == nama_produk, 'Harga (Rp)'] = harga
        if stok is not None:
            df.loc[df['Nama Produk'] == nama_produk, 'Stok (kg)'] = stok
        df.to_csv(filename_produk, index=False)

        clear()
        tampilkan_produk()
        print(f"\nProduk '{nama_produk}' berhasil diubah")
        input("\nKlik [ENTER] untuk kembali.")
        manage_produk() 

    else:
        print(f"\nProduk '{nama_produk}' tidak ditemukan.")
        input("\nKlik [ENTER] untuk kembali.")
        manage_produk()


def hapus_produk(nama_produk):
    df = pd.read_csv(filename_produk)
    if nama_produk in df['Nama Produk'].values:
        while True:
            confirm = input("\nYakin ingin menghapus produk? [y/n] : ")
            if confirm == "y":
                df = df[df['Nama Produk'] != nama_produk]
                df.to_csv(filename_produk, index=False)
                clear()
                tampilkan_produk()
                print(f"\nProduk '{nama_produk}' berhasil dihapus")
                input("\nKlik [ENTER] untuk kembali.")
                manage_produk()
                break 
            elif confirm == "n":
                manage_produk()
                break
            else:
                print("Pilihan tidak valid !!!")

    else:
        print(f"\nProduk '{nama_produk}' tidak ditemukan.")
        input("\nKlik [ENTER] untuk kembali.")
        manage_produk()


def manage_produk():
    df = pd.read_csv(filename_produk)
    clear()
    judul_halaman("H A L A M A N  M A N A G E  P R O D U K") 
    tabel_menu(menu_manage_produk)
    tabel_menu(back_out)
    pilihan = input("\nPilih : ")

    while pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" and pilihan != "b" and pilihan != "o":
        clear()
        judul_halaman("H A L A M A N  M A N A G E  P R O D U K") 
        tabel_menu(menu_manage_produk)
        tabel_menu(back_out)
        print("\nPilih menu yang tersedia !!!")
        pilihan = input("Pilih : ")

    if pilihan == '1':
        clear()
        tampilkan_produk()
        input("\nKlik [ENTER] untuk kembali.")
        manage_produk()

    elif pilihan == '2':
        clear()
        tampilkan_produk()
        while True:
            nama_produk = input("\nMasukkan nama produk : ")
            nama_produk = nama_produk.capitalize()
            if nama_produk in df["Nama Produk"].values:
                clear()
                tampilkan_produk()
                print("\nProduk telah tersedia, silahkan pilih nama lain !!!")
                continue
            else:
                clear()
                tampilkan_produk()
                print(f"\nMasukkan nama produk baru : {nama_produk}")
                harga = int(input("Masukkan harga : "))
                stok = int(input("Masukkan stok : "))
                tambah_produk(nama_produk, harga, stok)
                break
    
    elif pilihan == '3':
        clear()
        tampilkan_produk()
        nama_produk = input("\nNama Produk yang ingin diubah : ")
        nama_produk = nama_produk.capitalize()
        harga = input("Harga baru (tekan enter jika tidak ingin mengubah) : ")
        stok = input("Stok baru (tekan enter jika tidak ingin mengubah) : ")
        ubah_produk(nama_produk, int(harga) if harga else None, int(stok) if stok else None)

    elif pilihan == '4':
        clear()
        tampilkan_produk()
        nama_produk = input("\nNama Produk yang ingin dihapus : ")
        nama_produk = nama_produk.capitalize()
        hapus_produk(nama_produk)

    elif pilihan == 'b':
        menu_admin()

    elif pilihan == 'o':
        exit()


#====================================================================================================================
# FUNGSI MANAGE JASA PENGIRIMAN
#====================================================================================================================
def tampilkan_pengiriman():
    daftar_pengiriman = []
    with open("daftar_pengiriman.csv", "r") as file:
        lihat_data = csv.DictReader(file)
        for row in lihat_data:
            daftar_pengiriman.append(row)

    judul_halaman("D A F T A R  J A S A  P E N G I R I M A N")
    print(f"| No. |{"Nama Jasa Pengiriman".center(48)}|{"Biaya (Rp)".center(41)}|")
    print(f"|{"="*lebar}|")
    for i in range(len(daftar_pengiriman)):
        if i >= 9 :
            print(f"| {i+1}. |{daftar_pengiriman[i]["Nama Jasa"].center(48)}|{daftar_pengiriman[i]["Biaya (Rp)"].center(41)}|")
        else:
            print(f"| {i+1}.  |{daftar_pengiriman[i]["Nama Jasa"].center(48)}|{daftar_pengiriman[i]["Biaya (Rp)"].center(41)}|")
    print(f"|{"="*lebar}|")


def tambah_pengiriman(nama_jasa, biaya):
    df = pd.read_csv(filename_pengiriman)
    new_pengiriman = pd.DataFrame({'Nama Jasa': [nama_jasa], 'Biaya (Rp)': [biaya]})
    df = pd.concat([df, new_pengiriman], ignore_index=True)
    df.to_csv(filename_pengiriman, index=False)

    clear()
    tampilkan_pengiriman()
    print(f"\nJasa pengiriman '{nama_jasa}' berhasil ditambahkan.")
    input("\nKlik [ENTER] untuk kembali.")
    manage_pengiriman() 


def ubah_pengiriman(nama_jasa, biaya=None):
    df = pd.read_csv(filename_pengiriman)
    if nama_jasa in df['Nama Jasa'].values:
        if biaya is not None:
            df.loc[df['Nama Jasa'] == nama_jasa, 'Biaya (Rp)'] = biaya
        df.to_csv(filename_pengiriman, index=False)

        clear()
        tampilkan_pengiriman()
        print(f"\nJasa pengiriman '{nama_jasa}' berhasil diubah.")
        input("\nKlik [ENTER] untuk kembali.")
        manage_pengiriman()

    else:
        print(f"\nJasa pengiriman '{nama_jasa}' tidak ditemukan.")
        input("\nKlik [ENTER] untuk kembali.")
        manage_pengiriman()


def hapus_pengiriman(nama_jasa):
    df = pd.read_csv(filename_pengiriman)
    if nama_jasa in df['Nama Jasa'].values:
        while True:
            confirm = input("\nYakin ingin menghapus produk? [y/n] : ")
            if confirm == "y":
                df = df[df['Nama Jasa'] != nama_jasa]
                df.to_csv(filename_pengiriman, index=False)
                clear()
                tampilkan_pengiriman()
                print(f"\nJasa pengiriman '{nama_jasa}' berhasil dihapus.")
                input("\nKlik [ENTER] untuk kembali.")
                manage_pengiriman()
                break 
            elif confirm == "n":
                manage_produk()
                break
            else:
                print("Pilihan tidak valid !!!")

    else:
        print(f"\nJasa pengiriman '{nama_jasa}' tidak ditemukan.")
        input("\nKlik [ENTER] untuk kembali.")
        manage_pengiriman()


def manage_pengiriman():
    df = pd.read_csv(filename_pengiriman)
    clear()
    judul_halaman("H A L A M A N  M A N A G E  J A S A  P E N G I R I M A N") 
    tabel_menu(menu_manage_pengiriman1)
    tabel_menu(menu_manage_pengiriman2)
    tabel_menu(back_out)
    pilihan = input("\nPilih : ")

    while pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" and pilihan != "b" and pilihan != "o":
        clear()
        judul_halaman("H A L A M A N  M A N A G E  J A S A  P E N G I R I M A N") 
        tabel_menu(menu_manage_pengiriman1)
        tabel_menu(menu_manage_pengiriman2)
        tabel_menu(back_out)
        print("\nPilih menu yang tersedia !!!")
        pilihan = input("Pilih : ")

    if pilihan == '1':
        clear()
        tampilkan_pengiriman()
        input("\nKlik [ENTER] untuk kembali.")
        manage_pengiriman()

    elif pilihan == '2':
        clear()
        tampilkan_pengiriman()
        while True:
            nama_jasa = input("\nMasukkan nama produk baru : ")
            nama_jasa = nama_jasa.upper()
            if nama_jasa in df["Nama Jasa"].values:
                clear()
                tampilkan_pengiriman()
                print("\nProduk telah tersedia, silahkan pilih nama lain !!!")
                continue
            else:
                clear() 
                tampilkan_pengiriman()
                print(f"\nMasukkan nama jasa pengiriman baru : {nama_jasa}")
                biaya = int(input("\nMasukkan biaya : "))
                tambah_pengiriman(nama_jasa, biaya)
                break

    elif pilihan == '3':
        clear()
        tampilkan_pengiriman()
        nama_jasa = input("\nNama Jasa yang ingin diubah : ")
        nama_jasa = nama_jasa.upper()
        biaya = input("Biaya baru (tekan enter jika tidak ingin mengubah) : ")
        ubah_pengiriman(nama_jasa, int(biaya) if biaya else None)

    elif pilihan == '4':
        clear()
        tampilkan_pengiriman()
        nama_jasa = input("\nNama Jasa yang ingin dihapus : ")
        nama_jasa = nama_jasa.upper()
        hapus_pengiriman(nama_jasa)

    elif pilihan == 'b':
        menu_admin()

    elif pilihan == 'o':
        exit()


#====================================================================================================================
# MENU CUSTOMER
#====================================================================================================================
def menu_customer():
    clear()
    judul_halaman("M E N U  C U S T O M E R")
    tabel_menu(daftar_menu_customer)
    tabel_menu(back_out)
    pilihan = input("\nPilih : ")
    
    while pilihan != "1" and pilihan != "2" and pilihan != "b" and pilihan != "o":
        clear()
        tabel_menu(daftar_menu_admin)
        tabel_menu(back_out)
        print("\nPilih menu yang tersedia !!!")
        pilihan = input("Pilih : ")

    if pilihan == "1":
        clear()
        tampilkan_produk()
        input("\nKlik [ENTER] untuk kembali.")
        menu_customer()

    elif pilihan == "2":
        beli_produk()
        
    elif pilihan == "b":
        customer()
            
    elif pilihan == "o":
        exit()


#====================================================================================================================
# FUNGSI BELI PRODUK
#====================================================================================================================
daftar_produk = []
jumlah_produk = []
daftar_harga = []
total_sementara = []

def beli_produk():
    clear()
    tampilkan_produk()
    df = pd.read_csv(filename_produk)
    df.index = range(1, len(df) + 1)

    global total_harga
    total_harga = 0

    while True:
        pilihan = input("\nPilih nomor produk yang akan dibeli : ")

        if pilihan.isdigit() and 1 <= int(pilihan) <= len(df):
            index_pilihan = int(pilihan)
            global pilihan_produk
            pilihan_produk = df.loc[index_pilihan]

            nama_produk = df.at[index_pilihan, 'Nama Produk']
            harga_produk = df.at[index_pilihan, 'Harga (Rp)']
            global jumlah_pembelian
            jumlah_pembelian = int(input(f"Masukkan jumlah pembelian {pilihan_produk['Nama Produk']}: "))

            daftar_produk.append(nama_produk)
            jumlah_produk.append(jumlah_pembelian)
            daftar_harga.append(harga_produk)
            total_sementara.append(jumlah_pembelian*harga_produk)

            if 0 < jumlah_pembelian <= pilihan_produk['Stok (kg)']:
                df.at[index_pilihan, 'Stok (kg)'] -= jumlah_pembelian
                df.to_csv(filename_produk, index=False)
                total_harga += jumlah_pembelian*pilihan_produk["Harga (Rp)"]

                while True:
                    tambah_pembelian = input("\nIngin membeli produk lagi? [y/n] : ")
                    if tambah_pembelian == "y":
                        clear()
                        tampilkan_produk()
                        break

                    elif tambah_pembelian == "n":
                        clear()
                        tampilkan_produk()
                        input("\nKlik ENTER untuk lanjut ke halaman pengiriman.")
                        halaman_pengiriman()
                        break

                    else:
                        clear()
                        tampilkan_produk()
                        print("\nPilihan tidak valid !!!")

            elif jumlah_pembelian == 0:
                clear()
                tampilkan_produk()
                print("\nJumlah pembelian tidak boleh 0 !!!")

            else:
                clear()
                tampilkan_produk()
                print("\nStok produk tidak mencukupi, silahkan coba lagi dengan jumlah yang lebih kecil.")

        else:
            clear()
            tampilkan_produk()
            print("\nPilihan tidak valid, silahkan pilih nomor yang sesuai.")


#====================================================================================================================
# FUNGSI HALAMAN PENGIRIMAN
#====================================================================================================================
def halaman_pengiriman():
    clear()
    tampilkan_pengiriman()

    df = pd.read_csv(filename_pengiriman)
    df.index = range(1, len(df) + 1)

    while True:
        pilihan = input("\nPilih nomor jasa pengiriman : ")

        if pilihan.isdigit() and 1 <= int(pilihan) <= len(df):
            index_pilihan = int(pilihan)
            global nama_jasa
            nama_jasa = df.at[index_pilihan, 'Nama Jasa']
            global biaya_pengiriman
            biaya_pengiriman = df.at[index_pilihan, 'Biaya (Rp)']
            global total
            total = total_harga + biaya_pengiriman

            while True:
                global alamat
                alamat = input("\nMasukkan alamat pengiriman produk : ")
                if alamat == "":
                    clear()
                    tampilkan_pengiriman()
                    print("\nAlamat tidak boleh kosong !!!")
                else:
                    break

            input("\nKlik ENTER untuk lanjut ke halaman transaksi.")
            halaman_transaksi()
            break

        else:
            clear()
            tampilkan_pengiriman()
            print("\nPilihan tidak valid, silahkan pilih nomor yang sesuai.")


#====================================================================================================================
# FUNGSI HALAMAN TRANSAKSI
#====================================================================================================================
def halaman_transaksi():
    clear()
    judul_halaman("H A L A M A N  T R A N S A K S I")
    
    while True:
        print(f"\nTotal yang harus dibayar : {total}")
        global bayar
        bayar = input("\nMasukkan nominal yang akan dibayar : ")

        if not bayar.isdigit():
            clear()
            judul_halaman("H A L A M A N  T R A N S A K S I")
            print("\nNominal harus berupa angka !!!")
        else:
            bayar = int(bayar)
            if bayar < total:
                clear()
                judul_halaman("H A L A M A N  T R A N S A K S I")
                print("\nNominal tidak mencukupi.")
                
            else:
                global kembali
                kembali = bayar-total
                # Menyimpan data transaksi ke file csv dengan mencatat nama pengguna (username) yang sedang login
                transaksi_df = pd.DataFrame({
                    'Username': [username],
                    'Nama Produk': [daftar_produk],
                    'Jumlah Pembelian': [jumlah_produk],
                    'Jasa Pengiriman': [nama_jasa],
                    'Total Harga': [total],
                    'Alamat Pengiriman': [alamat],
                    'Tanggal Transaksi': [pd.to_datetime('today').strftime('%d-%m-%Y')]
                })
                # Menambahkan data transaksi ke dalam file transaksi.csv
                transaksi_df.to_csv("data_transaksi.csv", mode='a', header=not os.path.exists("data_transaksi.csv"), index=False)

                input("\nKlik [ENTER] untuk mencetak struk pembelian.")
                struk()
                break


#====================================================================================================================
# FUNGSI STRUK
#====================================================================================================================
def struk():
    clear()
    judul_halaman("S T R U K  P E M B E L I A N")
    
    # isi struk
    print("|",f"{pd.to_datetime('today').strftime('%d-%m-%Y')}         {username}".center(94),"|")
    print(f"|{"-"*lebar}|")
    for i in range(len(daftar_produk)):
        print(f"|                          {daftar_produk[i]}".ljust(lebar),"|")
        print(f"|                          {jumlah_produk[i]} x {daftar_harga[i]}                     =    Rp {total_sementara[i]}".ljust(lebar),"|")
    print(f"|{"-"*lebar}|")
    print(f"|                          Sub Total                     =    Rp {total_harga}".ljust(lebar),"|")
    print(f"|                          Biaya jasa pengiriman         =    Rp {biaya_pengiriman}".ljust(lebar),"|")
    print(f"|                          Total yang harus dibayar      =    Rp {total}".ljust(lebar),"|")
    print(f"|{"-"*lebar}|")
    print(f"|                          Tunai                         =    Rp {bayar}".ljust(lebar),"|")
    print(f"|                          Kembali                       =    Rp {kembali}".ljust(lebar),"|")
    print(f"|{"-"*(lebar)}|")
    print("|",f"Alamat pengiriman  :  {alamat}".center(94),"|")
    print(f"|{"-"*(lebar)}|")
    judul_halaman("TERIMA KASIH TELAH BERBELANJA DI BOOSTGRO MART !!!")
    
    input("\nKlik [ENTER] untuk kembali.")
    menu_customer()


#====================================================================================================================
# FUNGSI REKAP PENJUALAN
#====================================================================================================================
def rekap_penjualan():
    df = pd.read_csv('data_transaksi.csv')

    grup_df = df.groupby(['Username', 'Nama Produk', 'Jasa Pengiriman', 'Alamat Pengiriman', 'Tanggal Transaksi'], as_index=False)

    grup_df = grup_df[['Jumlah Pembelian', 'Total Harga']].sum()

    grup_df['No'] = range(1, len(grup_df) + 1)

    os.system('cls')
    print(f"|{"="*150}|")
    print("|",f">>>>>   B O O S T G R O  M A R T   <<<<<".center(148),"|")
    print("|",f"harga murah, transaksi mudah, kualitas mewah".center(148),"|")
    print(f"|{"="*150}|")
    print("|",f"D A T A  T R A N S A K S I  C U S T O M E R".center(148),"|")
    print(f"|{"="*150}|")

    print(grup_df[['No', 'Username', 'Nama Produk', 'Jumlah Pembelian', 'Jasa Pengiriman', 'Total Harga', 'Alamat Pengiriman', 'Tanggal Transaksi']].to_string(index=False))

    input("\nKlik ENTER untuk kembali!")
    menu_admin()



# MENJALANKAN PROGRAM
tampilan_awal()