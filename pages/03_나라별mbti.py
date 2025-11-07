import streamlit as st
import pandas as pd
import plotly.express as px

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="🌍 국가별 MBTI 분석", layout="wide")

# --- 데이터 불러오기 ---
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# --- 제목 ---
st.title("🌍 국가별 MBTI 비율 대시보드")
st.markdown("국가를 선택하면 MBTI 유형별 비율을 인터랙티브 막대 그래프로 보여줍니다.")

# --- 국가 선택 ---
country = st.selectbox("국가를 선택하세요:", sorted(df["Country"].unique()))

# --- 선택된 국가의 데이터 추출 ---
country_data = df[df["Country"] == country].iloc[0, 1:]  # 첫 행의 MBTI 데이터만 선택
country_df = pd.DataFrame({
    "MBTI": country_data.index,
    "비율": country_data.values
}).sort_values(by="비율", ascending=False)

# --- 색상 설정 ---
colors = ["#FF4B4B"] + px.colors.sequential.Viridis_r[1:15]  # 1등은 빨강, 나머지는 그라데이션
color_map = {mbti: colors[i] if i < len(colors) else "#cccccc" for i, mbti in enumerate(country_df["MBTI"])}

# --- 그래프 생성 ---
fig = px.bar(
    country_df,
    x="MBTI",
    y="비율",
    text=country_df["비율"].apply(lambda x: f"{x*100:.1f}%"),
    color="MBTI",
    color_discrete_map=color_map,
)

fig.update_traces(
    textposition="outside",
    marker_line_color="white",
    marker_line_width=1.5
)
fig.update_layout(
    title=f"🇺🇳 {country}의 MBTI 분포",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    showlegend=False,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    title_font_size=24
)

# --- 그래프 출력 ---
st.plotly_chart(fig, use_container_width=True)

# --- 참고 정보 ---
st.markdown("---")
st.caption("📊 데이터 출처: countriesMBTI_16types.csv | 시각화: Plotly + Streamlit")
