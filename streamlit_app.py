"""우리아이 육아노트 · 가족 보기 (Streamlit)

index.html(육아노트 앱)에 family.json(가족 공유 데이터)을 넣어서 보여 줍니다.
가족은 가입 없이 이 앱 주소만 열면 보기 전용 화면을 볼 수 있어요.
기록을 바꾸려면 Claude 육아노트 → 가족 공유 → family.json 저장 → 이 저장소의 family.json 교체.
"""
import json
import pathlib

import streamlit as st

st.set_page_config(
    page_title="우리아이 육아노트",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit 기본 메뉴·여백을 숨겨서 앱처럼 꽉 차게 보여 줍니다.
st.markdown(
    """
    <style>
      #MainMenu, header, footer,
      [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] {padding: 0 !important;}
      iframe {display: block; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

BASE = pathlib.Path(__file__).parent
MARK = "__FAMILY__"


@st.cache_data(ttl=60)
def load_page() -> str:
    html = (BASE / "index.html").read_text(encoding="utf-8")
    fam = "null"
    path = BASE / "family.json"
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("kids"):
                fam = (
                    json.dumps(data, ensure_ascii=False)
                    .replace("<", "\\u003c")
                    .replace("\u2028", "\\u2028")
                    .replace("\u2029", "\\u2029")
                )
        except (ValueError, AttributeError):
            fam = "null"
    return html.replace(MARK, fam, 1)


# 화면 높이: 주소 뒤에 ?h=1000 처럼 붙이면 바꿀 수 있어요 (기본 860).
try:
    height = int(st.query_params.get("h", 860))
except (TypeError, ValueError):
    height = 860
height = max(500, min(height, 3000))

page = load_page()
if hasattr(st, "iframe"):
    st.iframe(page, height=height)
else:  # 예전 Streamlit 버전용
    import streamlit.components.v1 as components

    components.html(page, height=height, scrolling=True)
