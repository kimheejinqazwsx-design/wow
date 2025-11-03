import streamlit as st

# Streamlit MBTI 진로 추천 앱 (추가 라이브러리 불필요)
# 청소년 친화적 톤, 이모지 사용

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯", layout="centered")

MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ",
]

# 각 MBTI에 대해 진로 2개, 적합 학과, 적합 성격(짧게)
MBTI_CAREERS = {
    "ISTJ": [
        {"career": "회계사 / 세무사 📊", "majors": ["경영학과", "회계학과"], "traits": ["꼼꼼함", "책임감", "규칙준수"]},
        {"career": "품질관리 / 시스템 관리자 🛠️", "majors": ["산업공학과", "전자공학과"], "traits": ["분석적 사고", "체계적", "신중함"]},
    ],
    "ISFJ": [
        {"career": "간호사 / 임상병리사 🩺", "majors": ["간호학과", "보건학과"], "traits": ["배려심", "인내심", "세심함"]},
        {"career": "교육행정 / 사회복지사 🤝", "majors": ["사회복지학과", "아동학과"], "traits": ["헌신적", "신뢰감", "조직적"]},
    ],
    "INFJ": [
        {"career": "상담심리사 / 임상심리사 💬", "majors": ["심리학과", "상담학과"], "traits": ["공감능력", "통찰력", "도덕성"]},
        {"career": "콘텐츠 기획 / 작가 ✍️", "majors": ["문예창작학과", "미디어학과"], "traits": ["창의적", "가치지향적", "섬세함"]},
    ],
    "INTJ": [
        {"career": "연구원 / 데이터 사이언티스트 🔬", "majors": ["수학과", "컴퓨터공학과", "통계학과"], "traits": ["전략적 사고", "독립적", "목표지향적"]},
        {"career": "전략 컨설턴트 🧭", "majors": ["경영학과", "경제학과"], "traits": ["분석적", "장기계획", "논리적"]},
    ],
    "ISTP": [
        {"career": "기계/전기 엔지니어 ⚙️", "majors": ["기계공학과", "전기공학과"], "traits": ["문제해결능력", "실용적", "즉흥적 응용"]},
        {"career": "소프트웨어 개발자 💻", "majors": ["컴퓨터공학과", "소프트웨어학과"], "traits": ["분석적", "실험정신", "독립적"]},
    ],
    "ISFP": [
        {"career": "디자이너 / 아티스트 🎨", "majors": ["시각디자인과", "공예과", "미술학과"], "traits": ["감성적", "미적 감각", "자유분방"]},
        {"career": "패션/사진작가 📸", "majors": ["패션디자인과", "사진학과"], "traits": ["창의성", "관찰력", "포용성"]},
    ],
    "INFP": [
        {"career": "작가 / 편집자 📝", "majors": ["국어국문학과", "문예창작학과"], "traits": ["이상주의", "상상력", "심층적 사고"]},
        {"career": "사회적기업가 / NGO 활동가 🌱", "majors": ["사회학과", "사회복지학과"], "traits": ["가치중심", "감수성", "지속성"]},
    ],
    "INTP": [
        {"career": "연구개발(R&D) / 학자 🧠", "majors": ["물리학과", "수학과", "컴퓨터공학과"], "traits": ["호기심", "논리적", "독창적 사고"]},
        {"career": "시스템 설계자 / 아키텍트 🏗️", "majors": ["소프트웨어학과", "전산학과"], "traits": ["추상화능력", "분석적", "독립성"]},
    ],
    "ESTP": [
        {"career": "영업/마케팅 담당자 📣", "majors": ["경영학과", "광고홍보학과"], "traits": ["적극적", "사교적", "위기대응능력"]},
        {"career": "응급구조사 / 현장 기술자 🚑", "majors": ["응급구조학과", "산업안전공학과"], "traits": ["빠른판단", "실행력", "스트레스강함"]},
    ],
    "ESFP": [
        {"career": "연예/엔터테인먼트 🎤", "majors": ["공연예술학과", "미디어학과"], "traits": ["표현력", "사교성", "즉흥성"]},
        {"career": "이벤트/서비스 기획자 🎉", "majors": ["관광경영학과", "경영학과"], "traits": ["사람중심", "창의적 실행", "유연함"]},
    ],
    "ENFP": [
        {"career": "창업가 / 스타트업 운영자 🚀", "majors": ["창업학과", "경영학과"], "traits": ["열정적", "사람을 이끄는 능력", "창의성"]},
        {"career": "콘텐츠 크리에이터 / SNS 마케터 📱", "majors": ["미디어학과", "광고홍보학과"], "traits": ["표현력", "트렌드 감각", "소통능력"]},
    ],
    "ENTP": [
        {"career": "제품기획 / 비즈니스 디벨로퍼 💡", "majors": ["경영학과", "산업디자인과"], "traits": ["아이디어 풍부", "토론능력", "유연한 사고"]},
        {"career": "변호사 / 정책분석가 ⚖️", "majors": ["법학과", "정치외교학과"], "traits": ["논쟁적 사고", "논리력", "설득력"]},
    ],
    "ESTJ": [
        {"career": "공기업/관리직 담당자 🏢", "majors": ["행정학과", "경영학과"], "traits": ["조직관리능력", "책임감", "결단력"]},
        {"career": "프로젝트 매니저 (PM) 📋", "majors": ["산업공학과", "경영정보학과"], "traits": ["체계적", "리더십", "시간관리"]},
    ],
    "ESFJ": [
        {"career": "초등교사 / 교육자 🏫", "majors": ["교육학과", "아동학과"], "traits": ["친절함", "관심기울임", "협력적"]},
        {"career": "HR/인사 담당자 🧾", "majors": ["경영학과", "심리학과"], "traits": ["대인관계능력", "조율능력", "책임감"]},
    ],
    "ENFJ": [
        {"career": "조직 리더 / 코치 🧑\u200d🏫", "majors": ["심리학과", "경영학과"], "traits": ["영향력", "공감능력", "비전제시"]},
        {"career": "PR/커뮤니케이션 전문가 🗣️", "majors": ["홍보학과", "미디어학과"], "traits": ["설득력", "사교성", "전략적 사고"]},
    ],
    "ENTJ": [
        {"career": "경영자 / CEO 🏆", "majors": ["경영학과", "경제학과"], "traits": ["리더십", "결단력", "전략적 마인드"]},
        {"career": "컨설턴트 / 투자분석가 📈", "majors": ["경영학과", "금융학과"], "traits": ["분석적", "설득력", "목표지향"]},
    ],
}

st.title("🎯 MBTI로 찾는 나에게 맞는 진로 - 청소년 버전")
st.write("안녕! MBTI 하나 골라줘~ 너한테 잘 맞는 진로 2가지를 알려줄게 :)")

with st.sidebar:
    st.header("설정")
    selected_mbti = st.selectbox("네 MBTI를 골라줘", MBTI_LIST)
    show_details = st.checkbox("자세한 설명 보기", value=True)

# 기본 안내
if not selected_mbti:
    st.info("왼쪽에서 MBTI를 선택해줘. 예: ENFP")
else:
    st.subheader(f"네 MBTI: {selected_mbti}")
    careers = MBTI_CAREERS.get(selected_mbti, [])

    if not careers:
        st.warning("아직 그 유형은 데이터가 없어. 다른 걸 골라줄래?")
    else:
        for idx, item in enumerate(careers, start=1):
            st.markdown(f"### {idx}. {item['career']}")
            st.write("**추천 학과:** " + ", ".join(item['majors']))
            st.write("**어울리는 성격:** " + ", \join(item['traits']))
            if show_details:
                # 친근한 청소년 말투로 한 줄 설명 추가
                if selected_mbti in ["ENFP", "ESFP", "ENTP"] and idx == 1:
                    extra = "에너지 넘치고 사람 만나는 걸 좋아하면 딱!"
                elif selected_mbti in ["INTJ", "INFJ"]:
                    extra = "깊게 파고들어서 높은 전문성이 나와요."
                else:
                    extra = "너의 강점을 살릴 수 있는 길이야."
                st.write(f"> {extra} 😊")
            st.divider()

# 다운로드 기능: 앱 코드 자체를 다운로드할 수 있게 함
app_code = """# 이 파일은 Streamlit로 실행되는 MBTI 진로 추천 앱입니다.
# Streamlit Cloud(Community Cloud)에서 바로 배포 가능합니다.
# 추가 라이브러리 설치 불필요 — streamlit만 필요합니다.

# (원본 코드와 동일)
"""

st.download_button(label="앱 코드 다운로드 (.py)", data=st.session_state.get('app_code', '') or '\n'.join([]), file_name="mbti_career_app.py", mime="text/x-python")

st.caption("※ 이 앱은 학습 참고용이에요. 다양한 경험과 상담도 함께 하길 추천해요! 💡")
