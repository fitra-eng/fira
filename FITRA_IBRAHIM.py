import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

global harga
option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Price list','Ordering','Give Rate And Suggestions On Our Service', 'Employee Salary')
)

if option == 'Home' or option == '':
    
    gambar1=Image.open('image/salon.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar1)
    nama="PROFIL BEAUTY QUEEN"
    st.markdown(f"<h1 style='text-align: center; color: black'>{nama}</h1>", unsafe_allow_html=True)
    long_sentence ="Beauty Queen Salon adalah perusahaan yang bergerak dibidang jasa kecantikan di Gorontalo yang didirikan oleh Queera Salsabila Anzalni. Beauty Queeen Salon berdiri sejak awal tahun 2019 tepatnya 09 juli 2019. Salon akan dioperasikan oleh satu manajer salon yang akan bekerja penuh waktu dan lima sampai 5-6 orang pegawai pendukung yang bekerja paruh waktu,Jam operasi salon adalah pkl. 09.00-19.00, setiap hari Senin-Minggu.  Pasar sasaran Beauty Queen Salon adalah wanita Pria dan remaja. Salon berlokasi di tempat yang mudah dijangkau dan tempatnya dipinggir jalan parkir yang luas.Perusahaan berharap tingkat pengunjung yang datang kembali tinggi. Dengan pengalaman lebih dari 5 tahun, kami telah membangun reputasi sebagai salah satu salon kecantikan terbaik di wilayah ini dengan tujuan mengembangkan layanan jasa yang positif dan proaktif yang akan dialami oleh konsumen setiap kali mereka datang ke Beauty Queen Salon.Kami berkomitmen memberikan pelayanan yang terbaik kepada setiap pelanggan kami, dengan harapan apabila setiap pelanggan yang datang tidak hanya satu kali berkunjung saja tetapi bisa menjadi pelanggan setia Beauty Queen Salon, maka interaksi dengan konsumen merupakan hal yang kritis dan merupakan kunci sukses bisnis ini. Pegawai memegang peranan penting dalam hal ini. Oleh karena itu, perusahaan menetapkan pegawai yang direkrut adalah orang-orang lulusan terbaik dan profesional, berpenampilan menarik dan gembira, teliti, cekatan, motivasi tinggi, dan yang memiliki komitmen untuk melayani konsumen. Perusahaan juga memberikan perhatian, pengembangan diri karyawan, dan kesejahteraan bagi hasil bagi para karyawannya agar dapat memberikan layanan yang prima. Salon yang dirancang pada interior dan perabotnya. Desain yang unik sangat diperhatikan untuk menjadi penambah daya tarik salon."
    st.write(f"<p style='text-align: justify; color: brown'>{long_sentence}</p>", unsafe_allow_html=True)
    
    gambar2=Image.open('image/pk.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar2)
elif option == 'Price list':
    gambar1=Image.open('image/salon.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar1)
    nama="DAFTAR HARGA"
    st.markdown(f"<h1 style='text-align: center; color: black'>{nama}</h1>", unsafe_allow_html=True)
    pesanan= pd.DataFrame({
    'Hair Treatment': ['Potong Rambut', 'Potong Cuci Tonik', 'Cuci Catok,Blow,curly', 'Smothing', 'Toning'],
    'Harga': [15000, 20000, 25000,150000,150000]
    })
    st.table(pesanan)

    pesanan= pd.DataFrame({
    'Hair Colouring': ['Pendek', 'Medium','Panjang','Highlight','Ombre'],
    'Harga': [100000, 120000, 200000,250000,200000]
    })

    st.table(pesanan)

    pesanan= pd.DataFrame({
    'Hair Spa/Mask': ['Pendek', 'Medium','Panjang','Creambath'],
    'Harga': [70000, 100000, 150000,200000]
    })

    st.table(pesanan)
    gambar2=Image.open('image/pk.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar2)
elif option == 'Ordering':
    gambar1=Image.open('image/salon.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar1)
    nama="PEMESANAN"
    st.markdown(f"<h1 style='text-align: center; color: black'>{nama}</h1>", unsafe_allow_html=True)
    layanan_treatment= ["Pilihan Layanan","Potong Rambut", "Potong Cuci Tonik", "Cuci Catok,Blow,curly", "Smothing", "Toning"]
    harga = [0,15000, 20000, 25000,150000,150000]

    pilih_layanan_treatment = st.selectbox("Hair Treatment", layanan_treatment, key="hair_treatment")

    if  pilih_layanan_treatment == "Pilih Layanan":
        st.write("Harga : 0")
    elif pilih_layanan_treatment == "Potong Rambut":
        st.write("Harga: Rp. 15.000")
    elif  pilih_layanan_treatment == "Potong Cuci Tonik":
        st.write("Harga: Rp. 20.000")
    elif  pilih_layanan_treatment == "Cuci Catok,Blow,curly":
        st.write("Harga: Rp. 25.000")
    elif  pilih_layanan_treatment == "Smothing":
        st.write("Harga: Rp. 150.000")  
    elif  pilih_layanan_treatment == "Toning":
        st.write("Harga: Rp. 150.000")

    layanan_colouring = ["Pilihan Layanan","Pendek", "Medium","Panjang","Highlight","Ombre"]
    harga_colouring = [0,100000, 120000, 200000,250000,200000]

    pilih_layanan_colouring = st.selectbox("Hair Colouring", layanan_colouring)

    if  pilih_layanan_colouring == "Pilih Layanan":
        st.write("Harga : 0")
    elif pilih_layanan_colouring == "Pendek":
        st.write("Harga: Rp. 100.000")
    elif  pilih_layanan_colouring == "Medium":
        st.write("Harga: Rp. 120.000")
    elif  pilih_layanan_colouring == "Panjang":
        st.write("Harga: Rp. 200.000")
    elif  pilih_layanan_colouring == "Highlight":
        st.write("Harga: Rp. 250.000")  
    elif  pilih_layanan_colouring == "Ombre":
        st.write("Harga: Rp. 200.000")

    layanan_spa = ["Pilihan Layanan","Pendek", "Medium","Panjang","Creambath"]
    harga_spa = [0,70000, 100000, 150000,200000]

    pilih_layanan_spa = st.selectbox("Hair Spa/Mask", layanan_spa)

    if  pilih_layanan_spa == "Pilih Layanan":
        st.write("Harga : 0")
    elif pilih_layanan_spa == "Pendek":
        st.write("Harga: Rp. 70.000")
    elif  pilih_layanan_spa == "Medium":
        st.write("Harga: Rp. 100.000")
    elif  pilih_layanan_spa == "Panjang":
        st.write("Harga: Rp. 150.000")
    elif  pilih_layanan_spa == "Creambath":
        st.write("Harga: Rp. 200.000")  

    Total_Pembayaran=0
    if pilih_layanan_treatment != "Pilih Layanan":
        Total_Pembayaran += harga[layanan_treatment.index(pilih_layanan_treatment)]

    if pilih_layanan_colouring != "Pilih Layanan":
        Total_Pembayaran += harga_colouring[layanan_colouring.index(pilih_layanan_colouring)]

    if pilih_layanan_spa != "Pilih Layanan":
        Total_Pembayaran += harga_spa[layanan_spa.index(pilih_layanan_spa)]
        
    st.markdown(f"<font color='brown'>Total Pembayaran : Rp. {Total_Pembayaran}</font>", unsafe_allow_html=True)

    

    change = 0
    if Total_Pembayaran > 0:
        change = int(st.number_input("Tunai : "))
    if change < Total_Pembayaran:
        st.markdown(f"<font color='brown'>Uang Yang Diberikan Tidak Cukup Untuk Membayar Total Pembayaran.</font>", unsafe_allow_html=True)
    else:
        st.markdown(f"<font color='brown'>Kembalian : Rp.{change - Total_Pembayaran}</font>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col3:
            st.markdown(f"<font color='grey'>Terimakasih Telah Mampir Di Queen Beauty Salon!</font>", unsafe_allow_html=True)


    gambar2=Image.open('image/pk.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar2)



elif option == 'Give Rate And Suggestions On Our Service':
    gambar1=Image.open('image/salon.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar1)
    nama="BERI NILAI DAN SARAN PADA PELAYANAN KAMI"
    st.markdown(f"<h1 style='text-align: center; color: black'>{nama}</h1>", unsafe_allow_html=True)
    
    pelayanan = ["Pilihan Layanan", "Hair Treatment", "Hair Colouring", "Hair Spa/Mask"]
    pilihan_pelayanan = st.selectbox("Pilih Pelayanan", pelayanan)

    if pilihan_pelayanan != "Pilihan Layanan":
        st.markdown(f"<font color='brown'>Pelayanan Yang Dipilih: {pilihan_pelayanan}</font>", unsafe_allow_html=True)

    nilai = st.slider("Berikan Nilai Pada Pelayanan", 1, 10)
    st.markdown(f"<font color='brown'>Nilai Yang Diberikan: {nilai}</font>", unsafe_allow_html=True)

    saran = st.text_input("Saran Untuk Pelayanan Kami")
    if st.button("Kirim"):
        kalimat="Terima kasih Telah Memberikan Nilai Serta Saran Pada Pelayanan Kami, Kedepannya Akan lebih Kami Perhatikan :)"
        st.markdown(f"<p style='text-align: center; color: grey'>{kalimat}</p>", unsafe_allow_html=True)

    gambar2=Image.open('image/pk.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar2)


elif option == 'Employee Salary':
    gambar1=Image.open('image/salon.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar1)
    nama="GAJI KARYAWAN "
    st.markdown(f"<h1 style='text-align: center; color: black'>{nama}</h1>", unsafe_allow_html=True)

    class Employee:
        def __init__(self, name, position, salary_per_day):
            self.name = name
            self.position = position
            self.salary_per_day = salary_per_day

        def calculate_salary(self, days_worked):
            return self.salary_per_day * days_worked

    def main():
        name = st.text_input("Nama Karyawan: ")
        position = ["Pilihan","Manager Salon", "Hair Treatment", "Hair Colouring", "Hair Spa/Mask"]
        position = st.selectbox("Posisi Karyawan", position)
        salary_per_day = st.number_input(" Gaji Per Hari: ")
        days_worked = st.number_input(" Jumlah Hari Kerja: ")

        employee = Employee(name, position, salary_per_day)
        total_salary = employee.calculate_salary(days_worked)

        
        if st.button("Cek"):
            st.markdown(f"<font color='brown'>Gaji {name} sebagai {position} adalah Rp {total_salary:,}</font>", unsafe_allow_html=True)
    if __name__ == "__main__":
        main()

    gambar2=Image.open('image/pk.png')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(gambar2)
    