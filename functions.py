import sqlite3
import pandas as pd


def tabloyap(tablo):
    conn=sqlite3.connect("final.sqlite3")
    c=conn.cursor()
    if tablo=="Ogrenci":
        komut="CREATE TABLE IF NOT EXISTS OGRENCILER (OGR_NO ,AD_SOYAD, SIFRE )"
        c.execute(komut)
        conn.commit()
    if tablo=="Ders":
        komut="CREATE TABLE IF NOT EXISTS DERSLER (DERS_ADI)"
        c.execute(komut)
        conn.commit()
    if tablo=="Notlar":
        komut="CREATE TABLE IF NOT EXISTS NOTLAR (NOT_NO INTEGER PRIMARY KEY AUTOINCREMENT,OGR_NO, AD_SOYAD, VIZE, FINAL )"
        c.execute(komut)
        conn.commit()
    if tablo=="Yoklama":
        komut="CREATE TABLE IF NOT EXISTS YOKLAMA (OGR_NO, ISIM, DURUM)"
        c.execute(komut)
        conn.commit()


def sqlrun(p_komut):
    conn=sqlite3.connect("final.sqlite3")
    c=conn.cursor()
    c.execute(p_komut)
    conn.commit()


def verigetir(komut):
    conn=sqlite3.connect("final.sqlite3")
    c=conn.cursor()
    c.execute(komut)
    veriler=c.fetchall()
    return veriler
    c.close


def ders_getir(getirici):
    if getirici=="Dersler":
        komut="SELECT DERS_ADI FROM DERSLER"
        conn=sqlite3.connect("final.sqlite3")
        c=conn.cursor()
        c.execute(komut)
        veriler=c.fetchall()
        veri_listesi = [veri[0] for veri in veriler]
        return veri_listesi
        c.close


def sifregetir(komut):
    conn=sqlite3.connect("final.sqlite3")
    c=conn.cursor()
    c.execute(komut)
    veriler=c.fetchone()
    return veriler[0] if veriler else None
    c.close


def tabloyugoster(p_veri, *sutunlar):
    df=pd.DataFrame(p_veri)
    df.columns=sutunlar
    return df
