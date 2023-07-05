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
        result = soup.find('span' , {'class' : 'waktu'}).text
        result = result.split(', ')
        Tanggal = result[0]
        Waktu = result [1]

        result = soup.find('div', {'class' : 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        Magnitudo = None
        Kedalaman = None
        LS = None
        BT = None
        Lokasi = None
        Dirasakan = None

        for res in result:

            if i == 1 :
                Magnitudo = res.text
            elif i == 2:
                Kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                LS = koordinat[0]
                BT = koordinat [1]
            elif i == 4:
                Lokasi = res.text

            elif i == 5:
                Dirasakan = res.text

            i = i +1


        Hasil = {
            'Tanggal' : Tanggal,
            'Waktu' : Waktu,
            'Magnitudo' : Magnitudo,
            'Kedalaman' : Kedalaman,
            'Koordinat' : {'LS' : LS , 'BT' : BT},
            'Lokasi' : Lokasi,
            'Dirasakan' : Dirasakan

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
    print(f"Koordinat: LS= {result['Koordinat']['LS']} , BT= {result['Koordinat']['BT']}")
    print(f"Lokasi: {result['Lokasi']}")
    print(f"Dirasakan: {result['Dirasakan']}")
