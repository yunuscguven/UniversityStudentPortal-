import streamlit as st
import functions as fun

# Bu sayfa öğretim görevlilerinin yönetim ve not giriş gibi işlemleri yapabileceği paneldir
st.subheader("Öğretim Görevlisi Paneli")
dersler=fun.ders_getir("Dersler")
tab1,tab2,tab3,tab4,tab5=st.tabs(["Ders Ekle","Öğrenci Kaydet","Sınav Girişi","Yoklama","Raporlama"])

with tab1:
    ders_adi=st.text_input("Dersin Adı")
    btn1=st.button("Ders Ekle")
    if btn1:
        if ders_adi=="":
            st.warning("Ders Adı Boş Geçilemez !")
        else:
            fun.tabloyap("Ders")
            komut=f"INSERT INTO DERSLER (DERS_ADI) VALUES('{ders_adi}')"
            fun.sqlrun(komut)
            st.success("Ders Başarıyla Eklendi")
with tab2:
    ogr_no=st.text_input("Öğrenci No")
    ogr_isim=st.text_input("İsim Soyisim")
    ogr_sifre=st.text_input("Şifrenizi Oluşturun")
    btn2=st.button("Ekle")
    if btn2:
        if ogr_no=="" or ogr_isim=="" or ogr_sifre=="":
            st.warning("Yukarıdaki Alanlar Boş Geçilemez !")
        else:
            fun.tabloyap("Ogrenci")
            komut=f"INSERT INTO OGRENCILER (OGR_NO, AD_SOYAD, SIFRE) VALUES ('{ogr_no}','{ogr_isim}','{ogr_sifre}')"
            fun.sqlrun(komut)
            st.success("Öğrenci Başarıyla Eklendi")

with tab3:
    ogr_no=st.text_input("*No")
    name=st.text_input("*Öğrenci İsim Soyisim")
    ders=st.selectbox("*Ders Seçiniz",dersler)
    vize=st.text_input("Vize Notu")
    final=st.text_input("Final Notu")
    if vize=="":
        vize=float(0)
    if final=="":
        final=float(0)
    btn3=st.button("Kaydet")
    if btn3:
        if ogr_no=="" or name=="" or ders=="":
            st.warning("Yıldızlı (*) Alanlar Boş Geçilemez !")
        else:
            notlandırma=(float(vize)*0.4)+(float(final)*0.6)
            if notlandırma <50:
                durum="KALDI"
            else:
                durum="GEÇTİ"
            fun.tabloyap("Notlar")
            komut=f"INSERT INTO NOTLAR (OGR_NO, AD_SOYAD, DERS, VIZE, FINAL, DURUM, NOTU) VALUES ('{ogr_no}','{name}','{ders}','{vize}','{final}','{durum}',{notlandırma})"
            fun.sqlrun(komut)
            st.success("Not Yükleme Başarılı")
with tab4:
    id=st.text_input("Öğrenci ID")
    isim=st.text_input("Öğrenici İsim Soyisim")
    yoklama=st.radio("Durumu",["Geldi", "Gelmedi"])
    btn4=st.button("Gir")
    btn_rapor=st.button("Yoklama Raporu Çek")
    if btn4:
        if id=="" or isim=="":
            st.warning("Yukarıdaki Alanlar Boş Geçilemez !")
        else:
            fun.tabloyap("Yoklama")
            komut=f"INSERT INTO YOKLAMA (OGR_NO, ISIM, DURUM) VALUES ('{id}','{isim}','{yoklama}')"
            fun.sqlrun(komut)
            st.success("Yoklama Kaydedildi")
    if btn_rapor:
        if id=="":
            st.warning("Öğrenci ID Girilmediği İçin Rapor Getirilemedi !")
        else:
            cmd=f"SELECT OGR_NO, ISIM, DURUM FROM YOKLAMA WHERE OGR_NO='{id}'"
            veriler=fun.verigetir(cmd)
            if len(veriler)>0:
                tablogoster=fun.tabloyugoster(veriler,"OGR_NO","ISIM","DURUM")
                st.table(tablogoster)
                st.success("Rapor Getirildi")
with tab5:
    with st.expander("Sınava Göre Rapor"):
        ogr_al=st.text_input("Sınav Raporu Öğrenci Numarası")
        btn5=st.button("Getir")
        if btn5:
            if ogr_al=="":
                st.warning("Öğrenci Numarası Girilmelidir !")
            else:
                cmd=f"SELECT OGR_NO, AD_SOYAD, DERS, VIZE, FINAL, NOTU FROM NOTLAR WHERE OGR_NO='{ogr_al}'"
                veriler=fun.verigetir(cmd)
                if len(veriler)>0:
                    tablogoster=fun.tabloyugoster(veriler,"OGR_NO","AD_SOYAD","DERS","VIZE","FINAL","NOTU")
                    st.table(tablogoster)
                    st.write("*final notu %60 - vize notu %40 üzerinden hesaplanmıştır")
                    st.success("Sınava Göre Rapor Oluşturuldu")

    with st.expander("Karne Raporu"):
        ogr_al=st.text_input("Karne Raporu Öğrenci Numarası")
        btn6=st.button("Oluştur")
        if btn6:
            if ogr_al=="":
                st.warning("Öğrenci Numarası Girilmelidir !")
            else:
                cmd=f"SELECT OGR_NO, AD_SOYAD, DERS, VIZE, FINAL, DURUM FROM NOTLAR WHERE OGR_NO='{ogr_al}'"
                veriler=fun.verigetir(cmd)
                if len(veriler)>0:
                    tablogoster=fun.tabloyugoster(veriler,"OGR_NO","AD_SOYAD","DERS","VIZE","FINAL","DURUM")
                    st.table(tablogoster)
                    st.write("*final notu %60 - vize notu %40 üzerinden hesaplanmıştır")
                    st.success("Karne Raporu Oluşturuldu")
