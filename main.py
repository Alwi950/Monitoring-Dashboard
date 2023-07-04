"""
Dashboard Monitori

"""


def ekstraksi_data():
    """
    Tanggal: 19 Juni 2023,
    Waktu :12:15:50 WIB
    Magnitudo:3.4
    Kedalaman: 10 km
    Lokasi: LU=1.17 , BT=121.07
    KeteranganPusat gempa berada di darat 21 km Barat Lakea
    Efek: Dirasakan (Skala MMI): II-III Tolitoli
    :return:
    """
    Hasil = {
        'Tanggal' : '19 Juni 2023',
        'Waktu' : '12:15:50 WIB',
        'Magnitudo' : 3.4 ,
        'Kedalaman' : '10 KM',
        'Lokasi' : { 'LU':1.17 , 'BT':121.07,},
        'Keterangan' : 'Pusat gempa berada di darat 21 km Barat Lakea',
        'Efek' : 'Dirasakan (Skala MMI): II-III Tolitoli'



    }
    return Hasil





def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG.go.id')
    print(f"Tanggal: {result['Tanggal']}")
    print(f"Waktu: {result['Waktu']}")
    print(f"Magnitudo: {result['Magnitudo']}")
    print(f"Kedalaman: {result['Kedalaman']}")
    print(f"Lokasi: LU= {result['Lokasi']['LU']} , BT= {result['Lokasi']['BT']}")
    print(f"Keterangan: {result['Keterangan']}")
    print(f"Efek: {result['Efek']}")


if __name__ == '__main__':
    print('Aplikasi Utama')

    result = ekstraksi_data()
    tampilkan_data(result)