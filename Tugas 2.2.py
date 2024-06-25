def sequential_search(names, target_name):
    
    for i in range(len(names)):
        if names[i] == target_name:
            return i
    return -1

def main():
    names = []
    n = int(input("Masukkan jumlah kategori buku : "))
    for i in range(n):
        name = input(f"Masukkan kategori buku ke-{i+1}:")
        names.append(name)
        
    target_name = input("Masukkan  buku yang akan dicari: ")
    
    result = sequential_search(names, target_name)
    
    if result != -1:
        print(f"Kategori Buku '{target_name}' ditemukan pada indeks {result}")
    else:
        print(f"Kategori Buku '{target_name}' tidak ditemukan dalam daftar")
        
if __name__=="__main__":
    main()