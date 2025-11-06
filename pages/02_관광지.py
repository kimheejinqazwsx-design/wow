import streamlit as st

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

# folium 로드 시도
try:
    import folium
    from folium.plugins import MarkerCluster
    from streamlit_folium import st_folium
except ModuleNotFoundError:
    st.error("❌ folium 모듈이 설치되지 않았어요! 😭\n\n"
             "✅ 해결 방법:\n"
             "1. 프로젝트 루트에 'requirements.txt' 파일을 만들고 아래 내용 추가:\n\n"
             "```\nstreamlit\nfolium\nstreamlit-folium\n```\n"
             "2. GitHub에 커밋 후 Streamlit Cloud에서 앱을 'Reboot' 또는 'Redeploy' 하세요.")
    st.stop()

# folium import가 성공한 경우 계속 실행
st.title("🇰🇷 외국인들이 사랑하는 서울 관광지 TOP 10")
st.markdown("서울의 인기 명소들을 지도로 확인해보세요 🗺️")

PLACES = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579026, "lon": 126.977969, "desc": "한복 인증샷 필수 👑"},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983677, "desc": "전통 한옥 골목 🏘️"},
    {"name": "명동 (Myeongdong)", "lat": 37.563828, "lon": 126.985160, "desc": "쇼핑 & 길거리 음식 🛍️🍡"},
    {"name": "N서울타워 (N Seoul Tower)", "lat": 37.551169, "lon": 126.988227, "desc": "서울 전망대 🌇"},
    {"name": "홍대 (Hongdae)", "lat": 37.556264, "lon": 126.923589, "desc": "라이브 공연 & 카페 🎸"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566295, "lon": 127.009356, "desc": "미래형 건축 ✨"},
    {"name": "인사동 (Insadong)", "lat": 37.574063, "lon": 126.985041, "desc": "전통 찻집과 공예 🍵"},
    {"name": "창덕궁 (Changdeokgung Palace)", "lat": 37.579620, "lon": 126.991033, "desc": "비밀의 정원 🌿"},
    {"name": "롯데월드타워 (Lotte World Tower)", "lat": 37.513084, "lon": 127.102501, "desc": "전망대 & 쇼핑몰 🏙️"},
    {"name": "이태원 (Itaewon)", "lat": 37.534467, "lon": 126.994995, "desc": "다국적 음식 거리 🍽️"}
]

# 사이드바 설정
with st.sidebar:
    st.header("지도 설정")
    zoom = st.slider("초기 줌 레벨", 10, 15, 12)
    center = st.selectbox("초기 중심 장소", [p["name"] for p in PLACES])

# 중심 좌표 설정
center_info = next(p for p in PLACES if p["name"] == center)

# folium 지도 생성
m = folium.Map(location=[center_info["lat"], center_info["lon"]], zoom_start=zoom)
cluster = MarkerCluster().add_to(m)

for p in PLACES:
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=f"<b>{p['name']}</b><br>{p['desc']}",
        tooltip=p["name"]
    ).add_to(cluster)

# 지도 출력
st.subheader("🗺️ 서울 관광지 지도")
st_folium(m, width=700, height=600)

# 리스트 출력
st.markdown("---")
st.subheader("📍 관광지 목록")
for i, p in enumerate(PLACES, start=1):
    st.markdown(f"**{i}. {p['name']}** — {p['desc']}")
