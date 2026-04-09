# AI Growth System

**B2B Sales & Marketing Automation powered by GPT-4o**  
GPT-4o 기반 B2B 세일즈 & 마케팅 자동화 시스템

---

## Overview / 프로젝트 개요

AI Growth System is a local web application that automates B2B sales and marketing workflows using OpenAI's GPT-4o model. Each agent is powered by a structured YAML prompt and accessible through a clean Streamlit dashboard.


---

## Tech Stack / 기술 스택

- **LLM**: OpenAI GPT-4o-mini
- **UI**: Streamlit
- **Prompt Management**: YAML
- **Config**: python-dotenv

---

## Agents / 에이전트 목록

| Agent | Description (EN) | 설명 (KR) |
|---|---|---|
| Lead Generation | Define ICP & prospect targeting strategy | ICP 정의 & 타겟 리스트 전략 |
| Lead Qualification | BANT/MEDDIC-based lead scoring | BANT/MEDDIC 기반 리드 스코어링 |
| Outreach Email | Personalized cold email generation | 개인화 콜드 이메일 자동 작성 |
| Content Creation | LinkedIn / blog / Twitter content | LinkedIn·블로그·트위터 콘텐츠 생성 |
| Content Strategy | Quarterly content planning | 분기별 콘텐츠 전략 플랜 |
| Social Listening | Buyer signals & monitoring strategy | 바이어 시그널 & 모니터링 전략 |
| SEO Analysis | Keyword clusters & organic growth | 키워드 클러스터 & 오가닉 성장 |
| Founder Strategy | Startup GTM & growth playbook | 스타트업 GTM & 성장 전략 |
| Deal Acceleration | Sales deal closing strategy | 세일즈 딜 클로징 전략 |

---

## Project Structure / 프로젝트 구조

```
ai-growth-system/
├── agents/
│   ├── base.py          # OpenAI API client & shared logic
│   └── __init__.py      # All agent functions
├── prompts/
│   └── *.yaml           # Per-agent prompt templates
├── ui/
│   └── app.py           # Streamlit dashboard
├── .env.example         # Environment variable template
├── requirements.txt
└── README.md
```

---

## Getting Started / 시작하기

### 1. Install dependencies / 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. Set up environment / 환경 변수 설정

```bash
cp .env.example .env
```

Open `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=sk-proj-...
```

### 3. Run / 실행

```bash
streamlit run ui/app.py
```

Open `http://localhost:8501` in your browser.

---

## How It Works / 작동 방식

1. Select an agent from the left panel
2. Enter your context in the text box (company info, prospect details, topic, etc.)
3. Click **Run** — GPT-4o generates a structured, actionable output

각 에이전트는 `prompts/` 폴더의 YAML 파일로 관리됩니다. 프롬프트만 수정하면 동작 방식을 코드 없이 바꿀 수 있습니다.

---

## Notes / 참고

- API key is never committed to this repo (`.gitignore` applied)
- All prompts are in English for optimal GPT-4o performance
- Prompts can be freely customized in `prompts/*.yaml`
