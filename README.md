# 🌱 우리아이 육아노트 · 가족 보기

가족이 **가입 없이** 웹 주소만 열어서 아이의 성장 기록·일기·접종 현황을 볼 수 있는 Streamlit 앱이에요.
기록은 보호자가 Claude의 육아노트에서 하고, `family.json` 파일로 이 앱에 반영해요.

## 들어 있는 파일

| 파일 | 역할 |
| --- | --- |
| `streamlit_app.py` | Streamlit 앱 (index.html에 family.json을 넣어 보여 줌) |
| `index.html` | 육아노트 앱 화면 |
| `family.json` | 가족에게 보여 줄 아이 기록 (보호자가 업데이트) |
| `requirements.txt` | 필요한 패키지 (streamlit) |

## 처음 한 번 올리기

1. **GitHub 저장소 만들기** — github.com → New repository → 이름 예: `yuga-note` → **Private(비공개)** 권장 → Create.
2. **파일 올리기** — 저장소 화면의 **Add file → Upload files** → 위 4개 파일을 끌어다 놓고 **Commit changes**.
3. **Streamlit에 게시** — share.streamlit.io → GitHub로 로그인 → **Create app** → 방금 만든 저장소, Branch `main`, Main file path `streamlit_app.py` → (원하면 App URL 지정, 예: `yuga-note-family`) → **Deploy**.
4. **공개 설정 확인** — 앱 화면 오른쪽 아래 **Manage app → Settings → Sharing**에서 누구나 볼 수 있게 되어 있는지 확인해요.
5. 생긴 주소(`https://○○○.streamlit.app`)를 가족 단톡방에 보내면 끝!

## 기록 업데이트하기

1. Claude 육아노트 → **👨‍👩‍👧 가족 공유** → **📦 family.json 저장**
2. GitHub 저장소 → `family.json` 선택 없이 **Add file → Upload files** 로 새 파일을 올려 덮어쓰기 → Commit
3. 1~2분 뒤 Streamlit 앱 새로고침 → 반영 완료

## 알아 두기

- 오랫동안 아무도 열지 않으면 Streamlit 앱이 잠들어요. 화면의 **Yes, get this app back up!** 버튼을 누르면 1분 안에 다시 켜져요.
- 앱 주소를 가진 사람은 누구나 아이 이름·생년월일·성장 기록을 볼 수 있어요. 믿을 수 있는 가족에게만 보내고, 이름 대신 애칭을 쓰면 더 안전해요.
- 저장소는 비공개(Private)로 두는 걸 권장해요. 공개 저장소면 family.json 내용이 GitHub에서 그대로 보여요.
- 지도 탭의 ‘현재 위치’는 Streamlit 화면 안에서 막혀 있어요. 도시 선택으로 기준을 바꿔 쓰세요.
- 화면 높이는 주소 뒤에 `?h=1000` 처럼 붙여서 바꿀 수 있어요.
- GitHub Pages로도 바로 볼 수 있어요: 저장소 Settings → Pages → Branch `main` → Save. `index.html`이 같은 폴더의 `family.json`을 자동으로 읽어요.
