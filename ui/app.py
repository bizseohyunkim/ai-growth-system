import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from agents import (
    lead_generation, lead_qualification, outreach_email,
    content_creator, content_strategy, social_listening,
    seo_analyzer, founder_strategy, deal_accelerator,
)

st.set_page_config(
    page_title="AI Growth System",
    page_icon=None,
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.stApp { background-color: #F7F6F3; }

section[data-testid="stSidebar"] { display: none; }

.block-container { padding: 3rem 4rem !important; max-width: 1200px; }

h1 {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 600 !important;
    color: #1A1A1A !important;
    letter-spacing: -0.03em !important;
    margin-bottom: 0.2rem !important;
}

hr { border: none !important; border-top: 1px solid #E8E6E1 !important; margin: 2rem 0 !important; }

div[data-testid="stRadio"] > label { display: none; }

div[data-testid="stRadio"] > div {
    display: flex;
    flex-direction: column;
    gap: 2px;
}

div[data-testid="stRadio"] > div > label {
    background: transparent !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 10px 14px !important;
    font-size: 0.875rem !important;
    font-weight: 400 !important;
    color: #555 !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
}

div[data-testid="stRadio"] > div > label:hover {
    background: #EEECEA !important;
    color: #1A1A1A !important;
}

div[data-testid="stRadio"] input[type="radio"] { display: none !important; }

textarea {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.82rem !important;
    background: #FFFFFF !important;
    border: 1px solid #E0DDD8 !important;
    border-radius: 8px !important;
    color: #1A1A1A !important;
    line-height: 1.6 !important;
}

textarea:focus { border-color: #1A1A1A !important; box-shadow: none !important; }

div[data-testid="stTextArea"] > label { display: none !important; }

div[data-testid="stButton"] > button {
    background: #1A1A1A !important;
    color: #F7F6F3 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.65rem 2rem !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.875rem !important;
    font-weight: 500 !important;
    width: 100% !important;
    transition: opacity 0.15s ease !important;
}

div[data-testid="stButton"] > button:hover {
    opacity: 0.75 !important;
    background: #1A1A1A !important;
    color: #F7F6F3 !important;
}

.result-box {
    background: #FFFFFF;
    border: 1px solid #E8E6E1;
    border-radius: 10px;
    padding: 1.8rem 2rem;
    font-size: 0.9rem;
    line-height: 1.75;
    color: #2A2A2A;
    margin-top: 1.5rem;
    white-space: pre-wrap;
}

h2 {
    font-size: 0.7rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #999 !important;
    margin-bottom: 1rem !important;
}

div[data-testid="column"]:first-child {
    border-right: 1px solid #E8E6E1;
    padding-right: 2rem !important;
}
</style>
""", unsafe_allow_html=True)


AGENTS = {
    "Lead Generation": {
        "fn": lead_generation,
        "placeholder": "Describe your company, product, and target market.\n\nExample:\nCompany: B2B SaaS startup\nProduct: AI-powered sales automation tool\nTarget: SMB sales teams\nCurrent customers: None (early stage)",
    },
    "Lead Qualification": {
        "fn": lead_qualification,
        "placeholder": "Paste lead details here.\n\nExample:\nName: John Smith, CTO\nCompany: Fintech startup (50 employees)\nNeed: Automate sales outreach\nBudget: Unknown\nTimeline: Next quarter",
    },
    "Outreach Email": {
        "fn": outreach_email,
        "placeholder": "Describe your prospect.\n\nExample:\nName: Sarah Lee, VP of Sales\nCompany: E-commerce SaaS (Series A)\nRecent news: Just closed funding round\nOur product: Sales automation solution",
    },
    "Content Creation": {
        "fn": content_creator,
        "placeholder": "Give me a topic or idea.\n\nExample:\n3 ways AI is tripling sales team productivity in 2025",
    },
    "Content Strategy": {
        "fn": content_strategy,
        "placeholder": "Describe your industry, company stage, and goals.\n\nExample:\nB2B HR SaaS, Series A, goal: 50 inbound leads/month",
    },
    "Social Listening": {
        "fn": social_listening,
        "placeholder": "Describe your brand, product, and market.\n\nExample:\nProduct: Sales automation SaaS\nCompetitors: Salesforce, HubSpot\nTarget: SMB sales managers in North America",
    },
    "SEO Analysis": {
        "fn": seo_analyzer,
        "placeholder": "Describe your product, seed keywords, and competitors.\n\nExample:\nProduct: Sales automation tool\nSeed keywords: CRM, sales management, outreach automation\nCompetitors: Apollo, Outreach.io",
    },
    "Founder Strategy": {
        "fn": founder_strategy,
        "placeholder": "Describe your startup stage and main challenge.\n\nExample:\nStage: Pre-seed\nProduct: B2B recruiting SaaS\nSituation: MVP done, 0 customers\nQuestion: How do we land our first 10 customers?",
    },
    "Deal Acceleration": {
        "fn": deal_accelerator,
        "placeholder": "Describe your current deal situation.\n\nExample:\nProspect: Enterprise IT team (500 employees)\nStage: Demo done, proposal sent\nBlocker: Waiting on procurement approval\nBudget: $30K/year\nTimeline: End of month",
    },
}

st.title("AI Growth System")
st.caption("B2B Sales & Marketing Automation powered by GPT-4o")
st.markdown("<hr>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2.5])

with col1:
    st.subheader("Agents")
    selected = st.radio("agent", list(AGENTS.keys()), label_visibility="collapsed")

with col2:
    agent = AGENTS[selected]
    st.subheader(selected.upper())

    user_input = st.text_area(
        "input",
        placeholder=agent["placeholder"],
        height=220,
        label_visibility="collapsed",
    )

    if st.button("Run", use_container_width=True):
        if not user_input.strip():
            st.warning("Please enter some input first.")
        else:
            with st.spinner("Analyzing..."):
                try:
                    result = agent["fn"](user_input)
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Error: {e}\n\nMake sure OPENAI_API_KEY is set in your .env file.")