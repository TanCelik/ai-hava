import streamlit as st
import requests

st.set_page_config(page_title="AI Stil Danışmanı", page_icon="👕")

st.title("👕 AI Stil Danışmanı")
st.write("Bulunduğunuz yerin havasına göre ne giymeniz gerektiğini öğrenin.")

# --- Hava Durumu Verisi Çekme ---
# Not: Normalde bir API key gerekir ama Open-Meteo ücretsiz ve anahtarsızdır.
def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url).json()
    return response['current_weather']

# --- Manuel Şehir Girişi (Konum izni her tarayıcıda çalışmayabilir) ---
# Streamlit Cloud'da direkt koordinat çekmek bazen zordur, o yüzden şehir seçtiriyoruz.
sehir = st.selectbox("Hangi şehirdesiniz?", ["Tekirdağ", "İstanbul", "Ankara", "İzmir", "Eskişehir", "Bursa"])

# Şehirlerin yaklaşık koordinatları (Örneğin senin üniversitenin olduğu yer)
coords = {
    "Tekirdağ": (40.97, 27.51),
    "İstanbul": (41.00, 28.97),
    "Ankara": (39.93, 32.85),
    "İzmir": (38.41, 27.12),
    "Eskişehir": (39.77, 30.52),
    "Bursa": (40.18, 29.06)
}

if st.button("Hava Durumuna Bak ve Tavsiye Ver"):
    lat, lon = coords[sehir]
    weather = get_weather(lat, lon)
    temp = weather['temperature']
    
    st.info(f"{sehir} için şu anki sıcaklık: {temp}°C")
    
    # --- Kıyafet Mantığı ---
    st.subheader("Stil Tavsiyesi:")
    if temp <= 10:
        st.warning("Hava oldukça soğuk! Kalın bir mont, atkı ve bere giymelisin.")
    elif 10 < temp <= 20:
        st.success("Hava serin. Bir sweatshirt veya hafif bir ceket işini görecektir.")
    elif 20 < temp <= 30:
        st.success("Hava güzel! Tişört ve rahat bir pantolon/şort giyebilirsin.")
    else:
        st.error("Hava çok sıcak! İnce, açık renkli kıyafetler seç ve mutlaka güneş kremi kullan.")

st.markdown("---")
st.caption("Veriler Open-Meteo üzerinden anlık alınmaktadır.")
