import streamlit as st
import functions as fun

# Bu Sayfa Öğrencilerin Giriş Yapıp Notlarını Görüntüleyebileceği ve Kayıt Olabileceği Paneldir
st.subheader("ÖĞRENCİ OTOMASYONUNA HOŞGELDİNİZ")

st.write("Giriş Yap")
numara=st.text_input("Öğrenci Numarası")
psw=st.text_input("Şifreniz")
btn1=st.button("Giriş")
if btn1:
    komut=f"SELECT SIFRE FROM OGRENCILER WHERE OGR_NO='{numara}'"
    sifre=fun.sifregetir(komut)
    if sifre==psw:
        st.success("Giriş Başarılı")
        cmd=f"SELECT OGR_NO, AD_SOYAD, DERS, VIZE, FINAL, NOTU, DURUM FROM NOTLAR WHERE OGR_NO='{numara}'"
        veriler=fun.verigetir(cmd)
        if len(veriler)>0:
            tablogoster=fun.tabloyugoster(veriler,"OGR_NO","AD_SOYAD","DERS","VIZE","FINAL","NOTU","DURUM")
            st.table(tablogoster)
            st.write("*final notu %60 - vize notu %40 üzerinden hesaplanmıştır")
    else:
        st.warning("Numara Veya Şifre Hatalı")

st.write("Öğrenci Hesabı Oluştur (Register)")
with st.expander("Kayıt Ol"):
    id=st.text_input("Öğrenci Numaranızı Gir")
    ogr_isim=st.text_input("İsim Soyisim")
    ogr_sifre=st.text_input("Şifrenizi Oluşturun")
    btn2=st.button("Kayıt Ol")
    if btn2:
        if id=="" or ogr_isim=="" or ogr_sifre=="":
            st.warning("Yukarıdaki Alanlar Boş Geçilemez !")
        else:
            fun.tabloyap("Ogrenci")
            komut=f"INSERT INTO OGRENCILER (OGR_NO, AD_SOYAD, SIFRE) VALUES ('{id}','{ogr_isim}','{ogr_sifre}')"
            fun.sqlrun(komut)
            st.success("Kaydınız Alındı, Oluşturduğunuz Şifre İle Giriş Sağlayabilirsiniz")
