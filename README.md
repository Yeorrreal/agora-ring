# 아고라 링

철학자들이 서성이는 아고라에서, 서로 맞서는 명제를 말하는 사람들을 링에 올려 싸움을 붙이고 키워드를 모으는 16비트 픽셀아트 추리 퍼즐. 지금은 3장 '정의'까지 플레이할 수 있다. 오른쪽 위 a/가 버튼으로 영어로도 할 수 있다.

**플레이**: https://yeorrreal.github.io/agora-ring/

- 철학자를 누르면 명제가 말풍선으로 뜨고, 계속 누르면 다른 명제로 바뀐다.
- 맞서는 명제를 띄운 사람들을 링으로 끌어다 놓고 종을 친다.
- 델포이의 신녀는 신탁(힌트)을 내리고, 콩밭에서는 오볼을 벌고, 물장수에게서는 물시계를 채운다.

## 빌드

```bash
npm install galmuri@2.39.3
python3 build.py
```

`agora-ring.src.html`이 소스이고, `build.py`가 Galmuri11 폰트와 효과음, 영어 문장을 넣어서 `index.html`을 만든다.

영어: `lang-en.txt`에 `한국어 ||| English` 한 줄씩. 대사·키워드·도감 같은 데이터 문장은 여기서 한국어 원문으로 찾아 바꾸고, 버튼·안내 문구는 소스 안에 `L('한국어','English')`로 나란히 있다. 철학자의 실제 말은 한국어를 다시 옮기지 않고 통용되는 영어 번역(Diels–Kranz 단편, Jowett의 플라톤)을 따른다.

폰트: [Galmuri](https://github.com/quiple/galmuri) (SIL Open Font License 1.1, [FONT-LICENSE.md](FONT-LICENSE.md))

효과음: 종소리와 펀치 소리는 Pixabay의 효과음("opening bell" #421471, "punch" #95294)을 잘라 `index.html` 안에 넣었다. 원본 파일(`sounds/`)은 저장소에 올리지 않으므로, 직접 빌드하려면 같은 파일을 `sounds/bell.mp3`, `sounds/punches.wav`로 두어야 한다. 나머지 소리(군중, 발소리, 부엉이)는 Web Audio로 합성한다.
