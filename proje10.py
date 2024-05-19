import sqlite3
import tkinter as tk


class VeritabaniYoneticisi:
    def __init__(self):
        self.baglanti = sqlite3.connect('musteri_satis_destek.db')
        self.cursor = self.baglanti.cursor()
        self.tablo_olustur()

    def tablo_olustur(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Musteri
                               (musteri_id INTEGER PRIMARY KEY,
                                musteri_adi TEXT,
                                iletisim_bilgileri TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Satis
                               (satis_id INTEGER PRIMARY KEY,
                                sunulan_urunler TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Destek
                               (destek_id INTEGER PRIMARY KEY,
                                destek_talep_numarasi TEXT,
                                talep_ozellikleri TEXT)''')

    def musteri_ekle(self, musteri_adi, iletisim_bilgileri):
        self.cursor.execute("INSERT INTO Musteri (musteri_adi, iletisim_bilgileri) VALUES (?, ?)",
                            (musteri_adi, iletisim_bilgileri))
        self.baglanti.commit()

    def satis_ekle(self, sunulan_urunler):
        self.cursor.execute("INSERT INTO Satis (sunulan_urunler) VALUES (?)",
                            (sunulan_urunler,))
        self.baglanti.commit()

    def destek_talebi_olustur(self, destek_talep_numarasi, talep_ozellikleri):
        self.cursor.execute("INSERT INTO Destek (destek_talep_numarasi, talep_ozellikleri) VALUES (?, ?)",
                            (destek_talep_numarasi, talep_ozellikleri))
        self.baglanti.commit()

    def musterileri_getir(self):
        self.cursor.execute("SELECT * FROM Musteri")
        return self.cursor.fetchall()

    def satislari_getir(self):
        self.cursor.execute("SELECT * FROM Satis")
        return self.cursor.fetchall()

    def destek_taleplerini_getir(self):
        self.cursor.execute("SELECT * FROM Destek")
        return self.cursor.fetchall()

    def __del__(self):
        self.baglanti.close()


class MusteriEklePenceresi:
    def __init__(self, master, veritabani):
        self.master = master
        self.master.title("Müşteri Ekle")

        self.veritabani = veritabani

        self.musteri_ekleme_arayuzu_olustur()

    def musteri_ekleme_arayuzu_olustur(self):
        musteri_ekleme_frame = tk.LabelFrame(self.master, text="Müşteri Ekle")
        musteri_ekleme_frame.pack(pady=10)

        musteri_adi_label = tk.Label(musteri_ekleme_frame, text="Müşteri Adı:")
        musteri_adi_label.grid(row=0, column=0)
        self.musteri_adi_entry = tk.Entry(musteri_ekleme_frame)
        self.musteri_adi_entry.grid(row=0, column=1)

        iletisim_bilgileri_label = tk.Label(musteri_ekleme_frame, text="İletişim Bilgileri:")
        iletisim_bilgileri_label.grid(row=1, column=0)
        self.iletisim_bilgileri_entry = tk.Entry(musteri_ekleme_frame)
        self.iletisim_bilgileri_entry.grid(row=1, column=1)

        musteri_ekle_button = tk.Button(musteri_ekleme_frame, text="Müşteri Ekle", command=self.musteri_ekle)
        musteri_ekle_button.grid(row=2, columnspan=2, pady=10)

    def musteri_ekle(self):
        musteri_adi = self.musteri_adi_entry.get()
        iletisim_bilgileri = self.iletisim_bilgileri_entry.get()
        self.veritabani.musteri_ekle(musteri_adi, iletisim_bilgileri)
        self.master.destroy()


class SatisEklePenceresi:
    def __init__(self, master, veritabani):
        self.master = master
        self.master.title("Satış Ekle")

        self.veritabani = veritabani

        self.satis_ekleme_arayuzu_olustur()

    def satis_ekleme_arayuzu_olustur(self):
        satis_ekleme_frame = tk.LabelFrame(self.master, text="Satış Ekle")
        satis_ekleme_frame.pack(pady=10)

        sunulan_urunler_label = tk.Label(satis_ekleme_frame, text="Sunulan Ürün:")
        sunulan_urunler_label.grid(row=0, column=0)
        self.sunulan_urunler_entry = tk.Entry(satis_ekleme_frame)
        self.sunulan_urunler_entry.grid(row=0, column=1)

        satis_ekle_button = tk.Button(satis_ekleme_frame, text="Satış Ekle", command=self.satis_ekle)
        satis_ekle_button.grid(row=1, columnspan=2, pady=10)

    def satis_ekle(self):
        sunulan_urunler = self.sunulan_urunler_entry.get()
        self.veritabani.satis_ekle(sunulan_urunler)
        self.master.destroy()


class DestekTalebiOlusturPenceresi:
    def __init__(self, master, veritabani):
        self.master = master
        self.master.title("Destek Talebi Oluştur")

        self.veritabani = veritabani

        self.destek_talebi_olusturma_arayuzu_olustur()

    def destek_talebi_olusturma_arayuzu_olustur(self):
        destek_talebi_olusturma_frame = tk.LabelFrame(self.master, text="Destek Talebi Oluştur")
        destek_talebi_olusturma_frame.pack(pady=10)

        destek_talep_numarasi_label = tk.Label(destek_talebi_olusturma_frame, text="Ürün Numarası:")
        destek_talep_numarasi_label.grid(row=0, column=0)
        self.destek_talep_numarasi_entry = tk.Entry(destek_talebi_olusturma_frame)
        self.destek_talep_numarasi_entry.grid(row=0, column=1)

        destek_musteri_numarasi_label = tk.Label(destek_talebi_olusturma_frame, text="Müşteri Numarası:")
        destek_musteri_numarasi_label.grid(row=1, column=0)
        self.destek_musteri_numarasi_entry = tk.Entry(destek_talebi_olusturma_frame)
        self.destek_musteri_numarasi_entry.grid(row=1, column=1)

        talep_ozellikleri_label = tk.Label(destek_talebi_olusturma_frame, text="Talep Sebebi:")
        talep_ozellikleri_label.grid(row=2, column=0)
        self.talep_ozellikleri_entry = tk.Entry(destek_talebi_olusturma_frame)
        self.talep_ozellikleri_entry.grid(row=2, column=1)

        destek_talebi_olustur_button = tk.Button(destek_talebi_olusturma_frame, text="Destek Talebi Oluştur",
                                                 command=self.destek_talebi_olustur)
        destek_talebi_olustur_button.grid(row=3, columnspan=2, pady=10)

    def destek_talebi_olustur(self):
        destek_talep_numarasi = self.destek_talep_numarasi_entry.get()
        talep_ozellikleri = self.talep_ozellikleri_entry.get()
        self.veritabani.destek_talebi_olustur(destek_talep_numarasi, talep_ozellikleri)
        self.master.destroy()


class ListelemePenceresi:
    def __init__(self, master, veritabani):
        self.master = master
        self.master.title("Listeleme")

        self.veritabani = veritabani

        self.listeleme_arayuzunu_olustur()

    def listeleme_arayuzunu_olustur(self):
        listeleme_frame = tk.LabelFrame(self.master, text="Listeleme")
        listeleme_frame.pack(pady=10)

        musteriler_label = tk.Label(listeleme_frame, text="Müşteriler:")
        musteriler_label.grid(row=0, column=0)

        self.musteriler_listbox = tk.Listbox(listeleme_frame, width=40)
        self.musteriler_listbox.grid(row=0, column=1)

        satislar_label = tk.Label(listeleme_frame, text="Satışlar:")
        satislar_label.grid(row=1, column=0)

        self.satislar_listbox = tk.Listbox(listeleme_frame, width=40)
        self.satislar_listbox.grid(row=1, column=1)

        destek_talepleri_label = tk.Label(listeleme_frame, text="Destek Talepleri:")
        destek_talepleri_label.grid(row=2, column=0)

        self.destek_talepleri_listbox = tk.Listbox(listeleme_frame, width=40)
        self.destek_talepleri_listbox.grid(row=2, column=1)

        self.musterileri_goster()
        self.satislari_goster()
        self.destek_taleplerini_goster()

    def musterileri_goster(self):
        musteriler = self.veritabani.musterileri_getir()
        for musteri in musteriler:
            self.musteriler_listbox.insert(tk.END, musteri)

    def satislari_goster(self):
        satislar = self.veritabani.satislari_getir()
        for satis in satislar:
            self.satislar_listbox.insert(tk.END, satis)

    def destek_taleplerini_goster(self):
        talepler = self.veritabani.destek_taleplerini_getir()
        for talep in talepler:
            self.destek_talepleri_listbox.insert(tk.END, talep)


class AnaPencere:
    def __init__(self, master):
        self.master = master
        self.master.title("Müşteri Satış Destek Uygulaması")

        self.veritabani = VeritabaniYoneticisi()

        self.ana_sayfa_arayuzunu_olustur()

    def ana_sayfa_arayuzunu_olustur(self):
        self.label = tk.Label(self.master, text="Müşteri İlişkileri Yönetimi Sistemine Hoşgeldiniz", font=("Helvetica", 14))
        self.label.pack(pady=10)

        musteri_ekle_button = tk.Button(self.master, text="Müşteri Ekle", command=self.musteri_ekle_penceresi_ac, width=20)
        musteri_ekle_button.pack(pady=10)

        satis_ekle_button = tk.Button(self.master, text="Satış Ekle", command=self.satis_ekle_penceresi_ac, width=20)
        satis_ekle_button.pack(pady=10)

        destek_talebi_button = tk.Button(self.master, text="Destek Talebi Oluştur", command=self.destek_talebi_olustur_penceresi_ac, width=20)
        destek_talebi_button.pack(pady=10)

        listeleme_button = tk.Button(self.master, text="Listeleme Penceresi Aç", command=self.listeleme_penceresi_ac, width=20)
        listeleme_button.pack(pady=10)

        kullanım_kılavuzu_button = tk.Button(self.master, text="Kullanım Kılavuzu", command=self.kullanım_kılavuzu_penceresi_ac, width=20)
        kullanım_kılavuzu_button.place(relx=0, rely=1.0, anchor='sw')

        cikis_button = tk.Button(self.master, text="Çıkış", command=self.master.destroy)
        cikis_button.place(relx=1.0, rely=1.0, anchor='se')

    def musteri_ekle_penceresi_ac(self):
        musteri_ekle_penceresi = tk.Toplevel(self.master)
        musteri_ekle_penceresi.title("Müşteri Ekle")
        musteri_ekle_uygulamasi = MusteriEklePenceresi(musteri_ekle_penceresi, self.veritabani)

    def satis_ekle_penceresi_ac(self):
        satis_ekle_penceresi = tk.Toplevel(self.master)
        satis_ekle_penceresi.title("Satış Ekle")
        satis_ekle_uygulamasi = SatisEklePenceresi(satis_ekle_penceresi, self.veritabani)

    def destek_talebi_olustur_penceresi_ac(self):
        destek_talebi_olustur_penceresi = tk.Toplevel(self.master)
        destek_talebi_olustur_penceresi.title("Destek Talebi Oluştur")
        destek_talebi_olustur_uygulamasi = DestekTalebiOlusturPenceresi(destek_talebi_olustur_penceresi, self.veritabani)

    def listeleme_penceresi_ac(self):
        listeleme_penceresi = tk.Toplevel(self.master)
        listeleme_penceresi.title("Listeleme")
        listeleme_uygulamasi = ListelemePenceresi(listeleme_penceresi, self.veritabani)

    def kullanım_kılavuzu_penceresi_ac(self):
        kullanım_kılavuzu_penceresi = tk.Toplevel(self.master)
        kullanım_kılavuzu_penceresi.title("Kullanım Kılavuzu")
        kullanım_kılavuzu_metin = """Kullanım Kılavuzu:
1. "Müşteri Ekle" butonuna tıklayarak yeni müşteriler ekleyebilirsiniz. 
2. "Satış Ekle" butonuyla yeni satışlar kaydedebilirsiniz.
3. "Destek Talebi Oluştur" ile müşterilerinizden gelen destek taleplerini kaydedebilirsiniz.
4. "Listeleme Penceresi Aç" butonu ile veritabanındaki müşterileri, satışları ve destek taleplerini listeleyebilirsiniz.
Bu sayfasında ki destek talepleri listesindeki ilk sütun ürün numarasını, ikinci sütun müşteri numarasını temsil ediyor.
Bu kısmı incelerseniz kimin hangi üründen destek talebi istediğini anlayabilirsiniz. 
5. "Çıkış" butonu ile uygulamadan çıkabilirsiniz.
6. "Kullanım Kılavuzu" butonu ile bu kılavuza erişebilirsiniz."""
        kullanım_kılavuzu_etiket = tk.Label(kullanım_kılavuzu_penceresi, text=kullanım_kılavuzu_metin, justify='left')
        kullanım_kılavuzu_etiket.pack(padx=10, pady=10)


root = tk.Tk()
uygulama = AnaPencere(root)
root.geometry("600x400")
root.mainloop()
