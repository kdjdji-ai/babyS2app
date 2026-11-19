"""우리아이 육아노트 · 가족 보기 (Streamlit)

index.html(육아노트 앱)에 가족 공유 데이터를 넣어서 보여 줍니다.
가족은 가입 없이 이 앱 주소만 열면 보기 전용 화면을 볼 수 있어요.

아이 기록은 GitHub 저장소가 아니라 Streamlit의 Secrets(비공개 설정)에 넣어요.
  Claude 육아노트 → 가족 공유 → 'Secrets 내용 복사'
  → Streamlit 앱 Manage app → Settings → Secrets 에 붙여 넣고 Save.
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


APP_VERSION = "2026-11-19 v3"


def read_family() -> tuple[dict | None, str]:
    """가족 데이터를 찾아서 (데이터, 상태 메시지)를 돌려줍니다."""
    raw, where = None, ""
    try:
        keys = list(st.secrets.keys())
    except Exception:  # Secrets가 없거나 형식(TOML)이 맞지 않음
        keys = []
        if not (BASE / "family.json").exists():
            return None, (
                "Secrets가 비어 있거나 형식이 맞지 않아요.\n\n"
                "① Manage app → ⋮ → Settings → Secrets에 streamlit-secrets.txt 내용을 "
                "처음부터 끝까지 그대로 붙여 넣고 Save 했는지 확인해 주세요.\n\n"
                "② 첫 줄은 FAMILY_JSON = 과 작은따옴표 3개, 마지막 줄은 작은따옴표 3개여야 해요. "
                "휴대폰에서 붙여 넣으면 작은따옴표(')가 ’ 로 바뀌어 형식이 깨질 수 있으니 PC에서 붙여 넣는 걸 권장해요."
            )
    for k in keys:  # FAMILY_JSON (대소문자 무관)
        if k.lower() == "family_json":
            raw, where = st.secrets[k], "Secrets"
            break
    if raw is None and keys:
        return None, "Secrets에 값은 있지만 FAMILY_JSON 항목이 없어요. 첫 줄이 FAMILY_JSON = 으로 시작하는지 확인해 주세요. (지금 항목: " + ", ".join(keys) + ")"
    if raw is None:
        path = BASE / "family.json"
        if path.exists():
            raw, where = path.read_text(encoding="utf-8"), "family.json"
    if raw is None:
        return None, "Secrets가 비어 있어요. Manage app → Settings → Secrets에 streamlit-secrets.txt 내용을 붙여 넣고 Save 해 주세요."
    if isinstance(raw, dict):
        data = raw
    else:
        text = str(raw).strip()
        try:
            data = json.loads(text)
        except ValueError:
            try:  # 휴대폰에서 붙여 넣을 때 따옴표가 “ ”로 바뀐 경우
                data = json.loads(text.replace("\u201c", '"').replace("\u201d", '"'))
            except ValueError as e:
                return None, f"{where}의 FAMILY_JSON 내용이 올바른 JSON이 아니에요. 다시 복사해서 붙여 넣어 주세요. ({e})"
    if not isinstance(data, dict) or not data.get("kids"):
        return None, f"{where}에 아이 정보(kids)가 없어요. 가족 공유에서 아이를 선택한 뒤 다시 복사해 주세요."
    return data, f"{where}에서 아이 {len(data['kids'])}명 정보를 불러왔어요."


def load_page() -> tuple[str, dict | None, str]:
    html = (BASE / "index.html").read_text(encoding="utf-8")
    data, status = read_family()
    fam = "null"
    if data:
        fam = (
            json.dumps(data, ensure_ascii=False)
            .replace("<", "\\u003c")
            .replace("\u2028", "\\u2028")
            .replace("\u2029", "\\u2029")
        )
    if MARK not in html:
        status = "index.html이 예전 버전이라 가족 데이터를 넣을 자리가 없어요. 새 zip의 index.html로 바꿔 올려 주세요."
        data = None
    return html.replace(MARK, fam, 1), data, status


# 화면 높이: 주소 뒤에 ?h=1000 처럼 붙이면 바꿀 수 있어요 (기본 860).
try:
    height = int(st.query_params.get("h", 860))
except (TypeError, ValueError):
    height = 860
height = max(500, min(height, 3000))

page, family, status = load_page()
if not family:
    st.markdown("<div style='padding-top:20px'></div>", unsafe_allow_html=True)
    st.warning("👨‍👩‍👧 가족 데이터를 불러오지 못했어요\n\n" + status + f"\n\n(앱 버전 {APP_VERSION})")
    st.stop()
if st.query_params.get("debug"):
    st.success(status + f" · 앱 버전 {APP_VERSION}")
if hasattr(st, "iframe"):
    st.iframe(page, height=height)
else:  # 예전 Streamlit 버전용
    import streamlit.components.v1 as components

    components.html(page, height=height, scrolling=True)
