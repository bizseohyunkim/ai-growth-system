# 🚀 AI Growth System

Claude API 기반 B2B 세일즈 & 마케팅 자동화 시스템

## 📦 설치

```bash
pip install -r requirements.txt
```

## ⚙️ 설정

```bash
cp .env.example .env
# .env 파일에 ANTHROPIC_API_KEY 입력
```

## 🚀 실행

```bash
streamlit run ui/app.py
```

## 🤖 에이전트 목록

| 에이전트 | 설명 |
|---|---|
| 리드 발굴 | ICP 정의 & 타겟 리스트 전략 |
| 리드 자격 분석 | BANT/MEDDIC 기반 스코어링 |
| 아웃리치 이메일 | 개인화 콜드 이메일 생성 |
| 콘텐츠 생성 | LinkedIn/블로그/트위터 콘텐츠 |
| 콘텐츠 전략 | 분기별 콘텐츠 플랜 |
| 소셜 리스닝 | 바이어 시그널 & 모니터링 전략 |
| SEO 분석 | 키워드 클러스터 & 오가닉 성장 |
| 파운더 전략 | 스타트업 GTM & 성장 전략 |
| 딜 가속화 | 세일즈 딜 클로징 전략 |

## 🗂️ 프로젝트 구조

```
ai-growth-system/
├── agents/
│   ├── base.py          # Claude API 연결 & 공통 로직
│   └── __init__.py      # 모든 에이전트 함수
├── prompts/
│   └── *.yaml           # 에이전트별 프롬프트
├── ui/
│   └── app.py           # Streamlit 대시보드
├── .env.example
├── requirements.txt
└── README.md
```
