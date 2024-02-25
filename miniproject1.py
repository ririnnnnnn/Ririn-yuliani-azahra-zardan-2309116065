class FreshBakery:
    def __init__(self, kode_roti, nama_roti, harga, stok):
        self.kode_roti = kode_roti
        self.nama_roti = nama_roti
        self.harga = harga
        self.stok = stok

class Manajemenroti:
    def __init__(self):
        self.daftar_roti = []

    def create_roti(self, kode_roti, nama_roti, harga, stok):
        for roti in self.daftar_roti:
            if roti.kode_roti == kode_roti:
                print("Kode roti yang Anda tambahkan sudah ada.")
                return
        self.daftar_roti.append(FreshBakery(kode_roti, nama_roti, harga, stok))
        print("Produk roti berhasil ditambahkan!")

    def read_roti(self):
        print("Berikut daftar roti yang tersedia:")
        for roti in self.daftar_roti:
            print(f"Kode Roti: {roti.kode_roti}, Nama Roti: {roti.nama_roti}, Harga: {roti.harga}, Stok: {roti.stok}")

    def update_roti(self, kode_roti, nama_roti=None, harga=None, stok=None):
        for roti in self.daftar_roti:
            if roti.kode_roti == kode_roti:
                if nama_roti:
                    roti.nama_roti = nama_roti
                if harga:
                    roti.harga = harga
                if stok:
                    roti.stok = stok
                print("Produk roti berhasil diupdate!")
                return
        print("Kode roti yang ingin Anda update tidak ditemukan.")

    def delete_roti(self, kode_roti):
        for roti in self.daftar_roti:
            if roti.kode_roti == kode_roti:
                self.daftar_roti.remove(roti)
                print("Produk roti berhasil dihapus.")
                return
        print("Kode roti yang ingin Anda hapus tidak ditemukan.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print (50*"=")
    print ("Welcome to Fresh Bakery!")
    print (50*"=")
    print("1. Menambahkan roti baru")
    print("2. Melihat daftar roti yg tersedia")
    print("3. Mengupdate roti yg tersedia")
    print("4. Menghapus roti")
    print("5. Keluar")
    print (50*"=")

# Contoh penggunaan program
manajemen_roti = Manajemenroti()

while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        kode_roti = input("Masukkan kode roti: ")
        nama_roti = input("Masukkan nama roti: ")
        harga = int(input("Masukkan harga roti: "))
        stok = int(input("Masukkan stok roti: "))
        manajemen_roti.create_roti(kode_roti, nama_roti, harga, stok)
    elif pilihan == '2':
        manajemen_roti.read_roti()
    elif pilihan == '3':
        kode_roti = input("Masukkan kode roti yang ingin diupdate: ")
        nama_roti = input("Masukkan nama roti baru (kosongkan jika tidak ingin mengubah): ")
        harga = input("Masukkan harga roti baru (kosongkan jika tidak ingin mengubah): ")
        stok = input("Masukkan stok roti baru (kosongkan jika tidak ingin mengubah): ")
        manajemen_roti.update_roti(kode_roti, nama_roti, harga, stok)
    elif pilihan == '4':
        kode_roti = input("Masukkan kode roti yang ingin dihapus: ")
        manajemen_roti.delete_roti(kode_roti)
    elif pilihan == '5':
        print("Terima kasih telah menggunakan program ini. Sampai Jumpa!")
        break
    else:
        print("Menu yg anda pilih tidak tersedia.")
