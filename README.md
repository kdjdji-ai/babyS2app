# 🌱 우리아이 육아노트 · 가족 보기

가족이 **가입 없이** 웹 주소만 열어서 아이의 성장 기록·일기·접종 현황을 볼 수 있는 Streamlit 앱이에요.
기록은 보호자가 Claude 육아노트에서 하고, **Streamlit Secrets(비공개 설정)** 로 이 앱에 반영해요.
아이 기록은 GitHub 저장소에 올라가지 않기 때문에 저장소를 **공개(Public)** 로 만들어도 안전해요.

## 들어 있는 파일

| 파일 | 역할 |
| --- | --- |
| `streamlit_app.py` | Streamlit 앱 (index.html에 Secrets의 가족 데이터를 넣어 보여 줌) |
| `index.html` | 육아노트 앱 화면 (아이 정보 없음) |
| `requirements.txt` | 필요한 패키지 (streamlit) |

## 처음 한 번 올리기

1. **새 공개 저장소 만들기** — github.com → New repository → 이름 예: `yuga-note-family` → **Public** → Create.
   - 예전에 family.json을 올렸던 비공개 저장소를 공개로 바꾸지 마세요. 커밋 기록에 아이 정보가 남아 있어요.
2. **파일 올리기** — **Add file → Upload files** → 위 3개 파일 + README.md를 끌어다 놓고 **Commit changes**.
3. **Streamlit에 게시** — share.streamlit.io → **Create app** → 새 저장소, Branch `main`, Main file path `streamlit_app.py`.
4. **Advanced settings → Secrets** 칸에 `streamlit-secrets.txt` 내용을 통째로 붙여 넣기 → **Deploy**.
   (나중에 넣어도 돼요: 앱 오른쪽 아래 **Manage app → ⋮ → Settings → Secrets**)
5. 생긴 주소(`https://○○○.streamlit.app`)를 가족 단톡방에 보내면 끝!

## 기록 업데이트하기

1. Claude 육아노트 → **👨‍👩‍👧 가족 공유** → **📋 Secrets 내용 복사** (또는 💾 파일로 저장)
2. Streamlit → **Manage app → Settings → Secrets** → 기존 내용을 지우고 붙여 넣기 → **Save**
3. 1분 안에 앱이 다시 시작되며 반영돼요. GitHub는 건드릴 필요 없어요.

## 알아 두기

- 오랫동안 아무도 열지 않으면 Streamlit 앱이 잠들어요. **Yes, get this app back up!** 을 누르면 1분 안에 다시 켜져요.
- 앱 주소를 가진 사람은 누구나 아이 이름·생년월일·성장 기록을 볼 수 있어요. 믿을 수 있는 가족에게만 보내고, 이름 대신 애칭을 쓰면 더 안전해요.
- 지도 탭의 ‘현재 위치’는 Streamlit 화면 안에서 막혀 있어요. 도시 선택으로 기준을 바꿔 쓰세요.
- 화면은 PC·휴대폰 창 크기에 맞춰 자동으로 꽉 차게 보여요.
