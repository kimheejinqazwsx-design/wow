import streamlit as st
import folium
from folium.plugins import MarkerCluster
import streamlit.components.v1 as components

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🇰🇷 외국인들이 사랑하는 서울 관광지 TOP 10")
st.markdown("지도를 확대하거나 마커를 클릭해보세요! 서울의 인기 명소들이 표시됩니다 🗺️")

# 관광지 데이터
PLACES = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579026, "lon": 126.977969, "desc": "조선의 대표 궁궐! 한복 입고 인증샷 필수 👑"},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983677, "desc": "전통 한옥이 모여 있는 예쁜 마을 🏘️"},
    {"name": "명동 (Myeongdong)", "lat": 37.563828, "lon": 126.985160, "desc": "쇼핑과 길거리 음식 천국! 🛍️🍡"},
    {"name": "N서울타워 (N Seoul Tower)", "lat": 37.551169, "lon": 126.988227, "desc": "서울을 한눈에! 야경이 최고 🌇"},
    {"name": "홍대 (Hongdae)", "lat": 37.556264, "lon": 126.923589, "desc": "젊음의 거리, 예술과 음악의 중심 🎸"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566295, "lon": 127.009356, "desc": "미래형 건축물과 야시장 ✨"},
    {"name": "인사동 (Insadong)", "lat": 37.574063, "lon": 126.985041, "desc": "전통 공예품과 찻집 거리 🍵"},
    {"name": "창덕궁 (Changdeokgung Palace)", "lat": 37.579620, "lon": 126.991033, "desc": "유네스코 세계유산, 비밀의 정원 🌿"},
    {"name": "롯데월드타워 (Lotte World Tower)", "lat": 37.513084, "lon": 127.102501, "desc": "대한민국 최고층 건물! 전망대 필수 🏙️"},
    {"name": "이태원 (Itaewon)", "lat": 37.534467, "lon": 126.994995, "desc": "세계 각국 음식과 문화가 공존 🍽️🌍"},
]

# 사이드바 설정
with st.sidebar:
    st.header("지도 설정")
    zoom = st.slider("초기 줌 레벨", 10, 15, 12)
    center = st.selectbox("초기 중심 장소", options=[p["name"] for p in PLACES])

# 선택한 중심지의 좌표 찾기
center_info = next(p for p in PLACES if p["name"] == center)

# 지도 생성
m = folium.Map(location=[center_info["lat"], center_info["lon"]], zoom_start=zoom)
marker_cluster = MarkerCluster().add_to(m)

# 마커 추가
for p in PLACES:
    popup_html = f"<b>{p['name']}</b><br>{p['desc']}<br><i>위도: {p['lat']}, 경도: {p['lon']}</i>"
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=p["name"]
    ).add_to(marker_cluster)

# 지도 출력
components.html(m._repr_html_(), height=700, scrolling=False)

# 하단 설명
st.markdown("---")
st.subheader("📍 관광지 목록")
for i, p in enumerate(PLACES, 1):
    st.markdown(f"**{i}. {p['name']}** — {p['desc']}")

st.caption("⚠️ 정보는 예시이며, 실제 방문 전 공식 사이트에서 확인하세요.")
