data_buku = {
'Pinjaman_1':
    {'nama_buku':'Thinking Fast & Slow', 
     'genre': 'Non Fiksi', 
     'index':'NF002003',
     'nama_peminjam' : 'Budi',
     'tanggal_pinjam':'01/01/2023',
     'tanggal_kembali' : '31/01/2023'},
    
'Pinjaman_2':
    {'nama_buku':'The Black Swan', 
     'genre': 'Non Fiksi', 
     'index':'NF002005',
     'nama_peminjam' : '-',
     'tanggal_pinjam':'-',
     'tanggal_kembali' : '-'},
    
'Pinjaman_3':
    {'nama_buku':'One Piece Chapter 117', 
     'genre': 'Komik', 
     'index':'KO001003',
     'nama_peminjam' : 'Udin',
     'tanggal_pinjam':'02/01/2023',
     'tanggal_kembali' : '02/02/2023'}
}
  
while True :   
    def main_menu():
        global opsi
        opsi = input('''
            Selamat Datang di Perpustakaan Saya!
          
            List Menu:
            1. Menampilkan Daftar Buku & Peminjam
            2. Tambah Buku & Peminjam
            3. Ubah Daftar Buku & Peminjam
            4. Hapus Buku & Peminjam
            5. Exit Program')
    
            Silahkan Pilih Main Menu dengan memasukkan angka 1-5 : ''')  
    main_menu()  
    
    while (not opsi == '1' and not opsi == '2' and not opsi == '3' and not opsi == '4' and not opsi == '5'):
        print ('''\n
               Pilihan yang Anda masukkan salah!
               Harap memasukkan input yang benar.
               ''')
        break

    while (opsi == '1'):
        def sub_menu_read(data):
            global opsi_read
            opsi_read = input('''
            ============= Report Data Buku & Peminjam =================    
            1. Tampilkan semua data
            2. Cari data tertentu
            3. Kembali ke menu utama
            Silahkan Pilih Menu Report dengan memasukkan angka 1-3 : ''')
        sub_menu_read(data_buku)
        while (not opsi_read == '1' and not opsi_read == '2' and not opsi_read == '3'):
            print ('''\n
               Pilihan yang Anda masukkan salah!
               Harap memasukkan input yang benar.
               ''')
            break
        while (opsi_read == '1'):
            a = ''
            print('\n')
            if data_buku == {}:
                print('Data tidak ditemukan')
            for keys,values in data_buku.items():
                isi = dict(values)
                for keys_1,values_1 in isi.items(): 
                   a = a+str(('{} : {}, '.format(keys_1,values_1)))
                print(a+'\n')
                a = ''

            break
        
        while (opsi_read == '2'):
            print('\n')
            cara_cari = input ('''
                    Pilih metode cari yang anda mau :
                    1. Nama buku
                    2. Index buku
                    3. Kembali ke menu sebelumnya
                    ''')

            if cara_cari == '3':
                break
            if not cara_cari == '1' and not cara_cari == '2' and not cara_cari =='3':
                print('''
                      Input yang Anda masukkan salah! 
                      ''')
            while cara_cari == '1':
                global cek_nama
                global cek_nama_data
                cari_nama_buku = input('''
                    Masukkan nama buku yang ingin dicari : 
                    ''')
                cek_nama = cari_nama_buku.upper()
                a = ''
                values = []
                for keys in data_buku.keys():
                    values.append(keys)
                for item in values:
                    index = values.index(item)
                    cek_nama_data = ''
                    for values_1 in data_buku[item]['nama_buku']:
                        cek_nama_data = cek_nama_data+values_1.upper()                 
                    if cek_nama == cek_nama_data :
                        for keys,values in data_buku[values[index]].items():
                            a = a+str(('{} : {}, '.format(keys,values)))
                        print(a)
                        break
                while cek_nama != cek_nama_data:
                    print('Data tidak ditemukan') 
                    break 
                break 
              
            while cara_cari == '2':
                global cek_index
                global cek_index_data
                cari_index_buku = input('''
                    Masukkan index buku yang ingin dicari : 
                    ''')
                cek_index = cari_index_buku.upper()
                a = ''
                values = []
                for keys in data_buku.keys():
                    values.append(keys)
                for item in values:
                    index = values.index(item)
                    cek_index_data = ''
                    for values_1 in data_buku[item]['index']:
                        cek_index_data = cek_index_data+values_1.upper()                 
                    if cek_index == cek_index_data :
                        for keys,values in data_buku[values[index]].items():
                            a = a+str(('{} : {}, '.format(keys,values)))
                        print(a)
                        break
                while cek_index != cek_index_data:
                    print('Data tidak ditemukan') 
                    break 
                break
                    
        if (opsi_read == '3'):
            break
   
    while (opsi == '2'):
        
        def sub_menu_create(data):
            global opsi_create
            opsi_create = input('''
            ============= Tambah Buku & Peminjam =================    
            1. Tambahkan data buku dan peminjam
            2. Kembali ke menu utama
            Silahkan Pilih Main Menu dengan memasukkan angka 1-2 : ''')
        sub_menu_create(data_buku)
        
        while (not opsi_create == '1' and not opsi_create == '2'):
            print ('''\n
               Pilihan yang Anda masukkan salah!
               Harap memasukkan input yang benar.
               ''')
            break
        
        while (opsi_create == '1'):        
            index_create = input('Masukkan kode baru untuk list buku yang mau anda tambahkan : ')
            cek_index = index_create.upper()
            if len(cek_index)!= 8:
                print('Kode harus terdiri dari 8 karakter')
                continue
            a = ''
            values = []
            
            if data_buku == {}:
                record = 'Pinjaman_1' 
                nama_buku = input('Masukkan data nama buku : ')
                genre = input('Masukkan data genre : ')
                nama_peminjam = input('Masukkan data nama peminjam : ')
                tanggal_pinjam = input('Masukkan data tanggal pinjam : ')
                tanggal_kembali = input('Masukkan data tanggal kembali : ')
                konfirmasi = input('''
                Apakah yakin untuk menyimpan data (Ya/Tidak)? '
                        ''')
                if (konfirmasi.upper()) == 'TIDAK' :
                    break
                if (konfirmasi.upper()) == 'YA' :
                    data_buku.update({record:
                    {
                    'nama_buku': nama_buku,
                    'genre': genre,
                    'index': str(index_create),
                    'nama_peminjam': nama_peminjam,
                    'tanggal_pinjam': tanggal_pinjam,
                    'tanggal_kembali': tanggal_kembali}})
                    print('Data berhasil tersimpan')
                break
                
            for keys in data_buku.keys():
                values.append(keys)
            for item in values:
                index = values.index(item)
                cek_index_data = ''
                for values_1 in data_buku[item]['index']:
                    cek_index_data = cek_index_data+values_1.upper()                 
                if cek_index == cek_index_data :
                    print ('Data duplikasi, harap masukkan kode lain')
                    break
            if cek_index == cek_index_data :
                break            
            if cek_index != cek_index_data :   
                list_kunci= []
            for item in data_buku.keys():
                list_kunci.append(item)
            index_kunci = len(list_kunci)+1
            
            record = list('Pinjaman_'+str(index_kunci)) 
            nama_buku = input('Masukkan data nama buku : ')
            genre = input('Masukkan data genre : ')
            nama_peminjam = input('Masukkan data nama peminjam : ')
            tanggal_pinjam = input('Masukkan data tanggal pinjam : ')
            tanggal_kembali = input('Masukkan data tanggal kembali : ')
            konfirmasi = input('''
                Apakah yakin untuk menyimpan data (Ya/Tidak)? '
                        ''')
            if (konfirmasi.upper()) == 'TIDAK' :
                break
            if (konfirmasi.upper()) == 'YA' :
                data_buku.update({record[0]:
                    {
                    'nama_buku': nama_buku,
                    'genre': genre,
                    'index': str(index_create),
                    'nama_peminjam': nama_peminjam,
                    'tanggal_pinjam': tanggal_pinjam,
                    'tanggal_kembali': tanggal_kembali}})
                print('Data berhasil tersimpan')
                break
            else :
                print('Input salah, harap masukkan kembali input yang benar')
                break
            
        if (opsi_create == '2'):
            break
    
    while (opsi == '3'):
        
        cek_update = ''
        cek_index_data = ''
        konfirmasi_ubah = ''
        konfirmasi_lanjut = ''
        lower_pilih_kolom = ''
        keys_1 = ''
        
        def menu_update():
            global opsi_update
            opsi_update = input('''
            ============= Ubah Daftar Buku & Peminjam =================    
            1. Ubah daftar buku & peminjam
            2. Kembali ke menu utama
            Silahkan Pilih Main Menu dengan memasukkan angka 1-2 : ''')
        menu_update()
        
        if (not opsi_update == '1' and not opsi_update == '2'):
            print ('''\n
               Pilihan yang Anda masukkan salah!
               Harap memasukkan input yang benar.
               ''')
            continue
        
        while (opsi_update == '1'):
            a = ''
            values = []
            konfirmasi_lanjut = ''
            index_update = input('Masukkan kode untuk list buku yang mau anda ubah : ')
            print('\n')
            cek_update = index_update.upper()
            if len(cek_update)!= 8:
                print('Kode harus terdiri dari 8 karakter')
                continue
            for keys in data_buku.keys():
                values.append(keys)
            for item_1 in values:
                index = values.index(item_1)
                cek_index_data = ''
                for values_1 in data_buku[item_1]['index']:
                    cek_index_data = cek_index_data+values_1.upper()                 
                if cek_update == cek_index_data :
                    for keys,values in data_buku[values[index]].items():
                        a = a+str(('{} : {}, '.format(keys,values)))
                    print(a)                    
                    break
            while cek_update == cek_index_data :
                konfirmasi_lanjut = input('''
                Apakah anda ingin melanjutkan
                proses Update (Ya/Tidak) ? 
                            ''')
                if not konfirmasi_lanjut.upper() == 'YA' and not konfirmasi_lanjut.upper() == 'TIDAK': 
                    print('Error, harap masukkan input yang sesuai')
                    continue
                break
            while konfirmasi_lanjut.upper() == 'YA':
                
                pilih_kolom = input('Pilih nama kolom yang akan diubah : ')
                lower_pilih_kolom = pilih_kolom.lower()
                a = ''
                cek_index_record = ''
                keys_data_buku = []
                konfirmasi_ubah = ''
                
                for keys_1 in data_buku[item_1].keys():
                    if lower_pilih_kolom == keys_1:
                        ubah = input ('Masukkan nilai baru : ')
                        while (True):
                            konfirmasi_ubah = input('''
                            Apakah Anda yakin untuk mengubah data (Ya/Tidak) ? 
                                    ''')
                            if not konfirmasi_ubah.upper()== 'YA'and not konfirmasi_ubah.upper()=='TIDAK':
                                print('Input yang dimasukkan error, harap coba lagi')
                                continue                               
                            elif konfirmasi_ubah.upper() == 'YA':
                                data_buku[item_1][lower_pilih_kolom] = ubah
                                print('Data berhasil diperbarui')
                                print('\n')
                                break
                            elif konfirmasi_ubah.upper()=='TIDAK':
                                break      
                    if lower_pilih_kolom != '' and keys_1 != '' and lower_pilih_kolom == keys_1 :
                            break  

                    elif lower_pilih_kolom == '' and keys_1 == '' and lower_pilih_kolom == keys_1 :
                        print('Kolom tidak tersedia, pilih nama kolom yang sesuai')                            
                        continue
                    
                if lower_pilih_kolom != '' and keys != '' and lower_pilih_kolom == keys_1 :       
                    break
            if cek_update != cek_index_data:
                print('Data tidak ditemukan')
                break            
            if lower_pilih_kolom != '' and keys != '' and lower_pilih_kolom == keys_1 :      
                break        
            if konfirmasi_lanjut.upper() == 'TIDAK':
                break
            break                                     
                
        if (opsi_update == '2'):
            break
        
    while (opsi == '4'):
        konfirmasi_lanjut = ''
        def menu_hapus():
            global opsi_delete
            opsi_delete = input('''
            ============= Hapus Buku & Peminjam =================    
            1. Hapus data buku & peminjam
            2. Hapus semua data
            3. Kembali ke menu utama
            Silahkan Pilih Main Menu dengan memasukkan angka 1-2 : ''')
        menu_hapus()
        if (not opsi_delete == '1' and not opsi_delete == '2' and not opsi_delete =='3'):
            print ('''\n
               Pilihan yang Anda masukkan salah!
               Harap memasukkan input yang benar.
               ''')
            continue
        while (opsi_delete == '1'):
            a = ''
            values = []
            konfirmasi_lanjut = ''
            index_delete = input('Masukkan kode untuk list buku yang mau anda hapus : ')
            print('\n')
            cek_delete = index_delete.upper()
            if len(cek_delete)!= 8:
                print('Kode harus terdiri dari 8 karakter')
                continue
            for keys in data_buku.keys():
                values.append(keys)
            for item_1 in values:
                index = values.index(item_1)
                cek_index_data = ''
                for values_1 in data_buku[item_1]['index']:
                    cek_index_data = cek_index_data+values_1.upper()                 
                if cek_delete == cek_index_data :
                    for keys,values in data_buku[values[index]].items():
                        a = a+str(('{} : {}, '.format(keys,values)))
                    print(a)                    
                    break
                elif cek_delete != cek_index_data:
                    print('Data yang Anda cari tidak ada!')
                    break
                break
                
            while cek_delete == cek_index_data :
                konfirmasi_lanjut = input('''
                Apakah anda ingin melanjutkan
                proses penghapusan (Ya/Tidak) ? 
                            ''')
                if not konfirmasi_lanjut.upper() == 'YA' and not konfirmasi_lanjut.upper() == 'TIDAK': 
                    print('Error, harap masukkan input yang sesuai')
                    continue
                break
            
            if konfirmasi_lanjut.upper() == 'TIDAK':
                break
            if konfirmasi_lanjut.upper() == 'YA':                             
                del data_buku[item_1]
                print('Data berhasil dihapus')
                print('\n')
                break  
        if (opsi_delete == '2'):
            konfirmasi_lanjut = input('''
                Apakah anda ingin melanjutkan
                proses penghapusan (Ya/Tidak) ? 
                            ''')
            if not konfirmasi_lanjut.upper() == 'YA' and not konfirmasi_lanjut.upper() == 'TIDAK': 
                print('Error, harap masukkan input yang sesuai')
                continue
            elif konfirmasi_lanjut.upper() == 'TIDAK':
                break
            elif konfirmasi_lanjut.upper() == 'YA':                             
                data_buku.clear()
                print('Seluruh data berhasil dihapus')
        if (opsi_delete == '3'):
            break        

    if (opsi == '5'):
        konfirmasi_exit = str(input('''
                Anda yakin ingin keluar (Ya/Tidak)? '''))
        if konfirmasi_exit.upper() == 'YA':
            break
        elif konfirmasi_exit.upper() == 'TIDAK':
            continue
        else :
            print('''
                Input yang anda masukkan salah!''')