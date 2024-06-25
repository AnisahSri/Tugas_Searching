def binary_search_sayur(sayuran, cari_sayuran, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if sayuran[mid] == cari_sayuran:
            return mid

        elif sayuran[mid] < cari_sayuran:
            low = mid + 1

        else:
            high = mid - 1

    return -1

# Daftar sayuran yang sudah diurutkan
sayuran = ["Bawang", "Bayam", "Brokoli", "Jagung", "Kangkung", "Kentang", "Kubis", "Lobak", "Sawi", "Selada", "Tomat"]

# Nama sayuran yang ingin dicari
cari_sayuran = "Cabai"

# Melakukan pencarian
hasil = binary_search_sayur(sayuran, cari_sayuran, 0, len(sayuran)-1)

# Menampilkan hasil
if hasil != -1:
    print(f"Sayuran '{cari_sayuran}' ditemukan di indeks {hasil}.")
else:
    print(f"Sayuran '{cari_sayuran}' tidak ditemukan dalam daftar.")
