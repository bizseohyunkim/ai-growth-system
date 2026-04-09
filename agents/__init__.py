from .base import run_agent

def lead_generation(company_info: str) -> str:
    """리드 발굴 & 프로스펙팅"""
    return run_agent("lead_generation.yaml", company_info)

def lead_qualification(lead_info: str) -> str:
    """리드 자격 분석 & 스코어링"""
    return run_agent("lead_qualification.yaml", lead_info)

def outreach_email(prospect_info: str) -> str:
    """개인화 이메일 작성"""
    return run_agent("outreach.yaml", prospect_info)

def content_creator(topic: str) -> str:
    """콘텐츠 생성 (포스트/블로그)"""
    return run_agent("content_creator.yaml", topic)

def content_strategy(industry: str) -> str:
    """콘텐츠 전략 & 인사이트"""
    return run_agent("content_strategy.yaml", industry)

def social_listening(brand_info: str) -> str:
    """소셜 리스닝 & 바이어 시그널"""
    return run_agent("social_listening.yaml", brand_info)

def seo_analyzer(keywords: str) -> str:
    """SEO & 오가닉 성장 전략"""
    return run_agent("seo_analyzer.yaml", keywords)

def founder_strategy(startup_info: str) -> str:
    """스타트업 / 파운더 전략"""
    return run_agent("founder_strategy.yaml", startup_info)

def deal_accelerator(deal_info: str) -> str:
    """세일즈 & 딜 가속화"""
    return run_agent("deal_accelerator.yaml", deal_info)
