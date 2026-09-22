import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(page_title="Canlı Evre Tahmini", layout="wide")

@st.cache_resource
def sistemi_hazirla():
    df = pd.read_csv("Thyroid.csv").dropna()
    y = df['Stage']
    X = pd.get_dummies(df.drop('Stage', axis=1))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model, X_train.columns

model, egitim_sutunlari = sistemi_hazirla()

st.title("🩺 Yeni Hasta İçin Canlı Evre Tahmini")
st.markdown("Doktor panelinden hastanın güncel muayene verilerini girin ve anlık evre tahminini görün.")

# --- KULLANICI GİRDİSİ FORMU ---
st.sidebar.header("📋 Hasta Giriş Formu")

# Kullanıcı bu kutucukları ve menüleri web sitesi üzerinden kendi seçecek
yas = st.sidebar.number_input("Hastanın Yaşı", min_value=15, max_value=90, value=45)
cinsiyet = st.sidebar.selectbox("Cinsiyet", ["F", "M"])
patoloji = st.sidebar.selectbox("Patoloji Tipi", ["Papillary", "Follicular", "Micropapillary"])
odak = st.sidebar.selectbox("Odaksallık (Focality)", ["Uni-focal", "Multi-focal"])
t_boyutu = st.sidebar.selectbox("Tümör Boyutu (T)", ["T1a", "T1b", "T2", "T3a", "T3b", "T4a", "T4b"])
lenf_n = st.sidebar.selectbox("Lenf Yayılımı (N)", ["N0", "N1a", "N1b"])
metastaz_m = st.sidebar.selectbox("Metastaz (M)", ["M0", "M1"])

if st.sidebar.button("Yapay Zeka Analizini Başlat"):
    # Kullanıcının formda seçtiği anlık verileri yakalıyoruz
    yeni_hasta_verisi = {
        'Age': yas,
        'Gender': cinsiyet,
        'Pathology': patoloji,
        'Focality': odak,
        'T': t_boyutu,
        'N': lenf_n,
        'M': metastaz_m,
        # Formu çok uzun tutmamak adına diğer faktörleri şimdilik risksiz varsayıyoruz
        'Smoking': 'No', 'Hx Smoking': 'No', 'Hx Radiothreapy': 'No',
        'Thyroid Function': 'Euthyroid', 'Physical Examination': 'Single nodular goiter-right',
        'Adenopathy': 'No', 'Risk': 'Low'
    }

    # Yeni hastayı makinenin anlayacağı 1 ve 0'lara çevirip sütunları hizalıyoruz
    yeni_df = pd.DataFrame([yeni_hasta_verisi])
    yeni_df_islenmis = pd.get_dummies(yeni_df)
    yeni_df_islenmis = yeni_df_islenmis.reindex(columns=egitim_sutunlari, fill_value=0)

    # Tahmin mekanizması çalışıyor
    tahmin = model.predict(yeni_df_islenmis)[0]

    st.success(f"🚨 **Yapay Zeka Tahmini (Klinik Evre): {tahmin}**")
    st.info("Bu sonuç, yandaki formda girdiğiniz verilere dayanarak saniyeler içinde sıfırdan hesaplanmıştır.")
