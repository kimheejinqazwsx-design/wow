import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="지역별 인구 시각화", page_icon="👥", layout="wide")

# 제목
st.title("📊 지역별 연령대 인구 시각화 대시보드")
st.write("선택한 지역의 연령대별 인구분포를 확인해보세요!")

# 데이터 불러오기
@st.cache_data
def load_data():
    # 한국어 CSV 인코딩 고려
    return pd.read_csv("population.csv.csv", encoding="cp949")

df = load_data()

# 데이터 기본 확인
if df is None or df.empty:
    st.error("데이터를 불러올 수 없습니다. 파일명을 확인해주세요.")
    st.stop()

# 지역 선택
regions = sorted(df["지역"].unique())
selected_region = st.selectbox("📍 지역을 선택하세요", regions)

# 선택한 지역의 데이터 필터링
filtered_df = df[df["지역"] == selected_region]

# 그래프 생성
fig = px.line(
    filtered_df,
    x="나이",
    y="인구수",
    title=f"👥 {selected_region}의 연령대별 인구 변화",
    markers=True,
    line_shape="spline"
)
fig.update_layout(
    xaxis_title="나이",
    yaxis_title="인구수",
    template="plotly_white",
    hovermode="x unified"
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# 데이터 테이블 보기 옵션
with st.expander("📋 데이터 테이블 보기"):
    st.dataframe(filtered_df)
