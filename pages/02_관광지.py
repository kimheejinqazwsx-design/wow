# streamlit_seoul_top10.py
# Streamlit app that uses folium to show "Top 10 Seoul tourist spots popular with foreigners"
# Works on Streamlit Cloud. No extra frontend libraries required.

import streamlit as st
import folium
from folium.plugins import MarkerCluster
import streamlit.components.v1 as components

st.set_page_config(page_title="Seoul Top10 (for foreigners)", layout="wide")

st.title("🇰🇷 Seoul Top 10 Tourist Spots (외국인 인기 장소)")
st.markdown("간단한 설명: 지도에서 장소를 클릭하면 간단한 설명이 나와요. 스트림릿 클라우드에서 바로 작동합니다.")

# Top-10 list: name, latitude, longitude, short description
PLACES = [
    {"name": "Gyeongbokgung Palace (경복궁)", "lat": 37.579026, "lon": 126.977969, "desc": "Historic royal palace — must-see for hanbok photos! 👑"},
    {"name": "Bukchon Hanok Village (북촌한옥마을)", "lat": 37.582604, "lon": 126.983677, "desc": "Traditional hanok neighborhood — great alleyway strolls. 🏘️"},
    {"name": "Myeongdong (명동)", "lat": 37.563828, "lon": 126.985160, "desc": "Shopping & street food heaven — K-beauty & snacks. 🛍️🍡"},
    {"name": "N Seoul Tower / Namsan Tower (N서울타워)", "lat": 37.551169, "lon": 126.988227, "desc": "Panoramic views of Seoul — best at sunset. 🌇"},
    {"name": "Hongdae / Hongik Univ. (홍대)", "lat": 37.556264, "lon": 126.923589, "desc": "Youth culture, live music, cafés — energetic vibe. 🎸☕"},
    {"name": "Dongdaemun Design Plaza (DDP, 동대문디자인플라자)", "lat": 37.566295, "lon": 127.009356, "desc": "Futuristic architecture & night markets. 🏛️✨"},
    {"name": "Insadong (인사동)", "lat": 37.574063, "lon": 126.985041, "desc": "Traditional crafts, tea houses, souvenirs. 🍵🖼️"},
    {"name": "Changdeokgung Palace & Huwon (창덕궁)", "lat": 37.579620, "lon": 126.991033, "desc": "UNESCO site with secret garden (Huwon). 🌿"},
    {"name": "Lotte World Tower / Seoul Sky (롯데월드타워)", "lat": 37.513084, "lon": 127.102501, "desc": "Tallest building in Korea — observation deck & mall. 🏙️"},
    {"name": "Itaewon (이태원)", "lat": 37.534467, "lon": 126.994995, "desc": "International food & nightlife district. 🍽️🌍"}
]

# Sidebar controls
with st.sidebar:
    st.header("지도 설정")
    zoom = st.slider("초기 줌 레벨", min_value=10, max_value=15, value=12)
    start_place = st.selectbox("초기 중심 위치 선택", options=[p['name'] for p in PLACES], index=0)

# find center coords for chosen start_place
center = next((p for p in PLACES if p['name'] == start_place), PLACES[0])

# Create folium map
m = folium.Map(location=[center['lat'], center['lon']], zoom_start=zoom)

# Add marker cluster
cluster = MarkerCluster().add_to(m)

for p in PLACES:
    popup_html = f"<b>{p['name']}</b><br>{p['desc']}<br><i>위도: {p['lat']}, 경도: {p['lon']}</i>"
    folium.Marker(
        location=[p['lat'], p['lon']],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=p['name']
    ).add_to(cluster)

# Add a small legend as a FloatImage (using Custom CSS via HTML)
legend_html = '''
     <div style="position: fixed; 
                 bottom: 50px; left: 50px; width: 220px; height: 110px; 
                 background-color: white; z-index:9999; font-size:14px; 
                 border:2px solid grey; padding:10px; border-radius:8px;">
     <b>📍 Seoul Top10 (for foreigners)</b><br>
     Click markers for details.<br>
     Tip: zoom in/out and click clusters to expand.
     </div>
     '''
m.get_root().html.add_child(folium.Element(legend_html))

# Render map in Streamlit using components.html
map_html = m._repr_html_()
components.html(map_html, height=700, scrolling=True)

st.markdown("---")
col1, col2 = st.columns([2,1])
with col1:
    st.subheader("장소 리스트")
    for i, p in enumerate(PLACES, start=1):
        st.markdown(f"**{i}. {p['name']}** — {p['desc']}")
with col2:
    st.subheader("간단 사용법")
    st.write("• 지도에서 마커 클릭 → 팝업 확인")
    st.write("• 사이드바에서 초기 중심 위치와 줌을 바꿔보세요")

st.caption("데이터는 예시용으로 제공됩니다 — 실제 방문 전 운영시간/요금은 공식 사이트에서 확인하세요.")

# End of app

# requirements.txt content (also included with this file below)
# -------------------
# streamlit
# folium
#
# If you'd prefer streamlit-folium for tighter integration, add:
# streamlit-folium
# -------------------
