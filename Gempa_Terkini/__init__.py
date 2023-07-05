import bs4
import requests


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200 :
        soup = bs4.BeautifulSoup(content.text, 'html.parser')
        result=soup.find(span , {'class' : 'waktu'})

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
    else:
        return None





def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menampilkan data terkini')
        return
    print('Gempa Terakhir Berdasarkan BMKG.go.id')
    print(f"Tanggal: {result['Tanggal']}")
    print(f"Waktu: {result['Waktu']}")
    print(f"Magnitudo: {result['Magnitudo']}")
    print(f"Kedalaman: {result['Kedalaman']}")
    print(f"Lokasi: LU= {result['Lokasi']['LU']} , BT= {result['Lokasi']['BT']}")
    print(f"Keterangan: {result['Keterangan']}")
    print(f"Efek: {result['Efek']}")
