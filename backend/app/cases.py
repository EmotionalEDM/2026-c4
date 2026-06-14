"""5 个预置展示案例（与展示逻辑设计文档完全一致）。"""
from __future__ import annotations

DEFAULT_SKILL = "code_review"

CASES: list[dict] = [
    {
        "case_id": "buyer1_clean",
        "title": "Buyer 1 · 无攻击",
        "skill_id": DEFAULT_SKILL,
        "buyer_id": "buyer1",
        "attack": "none",
        "difficulty": "baseline",
        "goal": "买家1+理想情况下，所有权与溯源都干净命中（基线）。",
    },
    {
        "case_id": "buyer1_attack_type1",
        "title": "Buyer 1 · 第一类攻击",
        "skill_id": DEFAULT_SKILL,
        "buyer_id": "buyer1",
        "attack": "type1_rewrite",
        "difficulty": "oblivious_attack",
        "goal": "买家1+改写，水印依然存活、溯源依然命中。",
    },
    {
        "case_id": "buyer1_attack_type2",
        "title": "Buyer 1 · 第二类攻击",
        "skill_id": DEFAULT_SKILL,
        "buyer_id": "buyer1",
        "attack": "type2_watermark_suppression",
        "difficulty": "adaptive_attack",
        "goal": "买家1+定向删审计条款（最难场景），分数略降但仍稳定判对。",
    },
    {
        "case_id": "buyer2_clean",
        "title": "Buyer 2 · 无攻击",
        "skill_id": DEFAULT_SKILL,
        "buyer_id": "buyer2",
        "attack": "none",
        "difficulty": "baseline",
        "goal": "买家2+理想情况下，所有权与溯源都干净命中（基线）。",
    },
    {
        "case_id": "buyer2_attack_type1",
        "title": "Buyer 2 · 第一类攻击",
        "skill_id": DEFAULT_SKILL,
        "buyer_id": "buyer2",
        "attack": "type1_rewrite",
        "difficulty": "oblivious_attack",
        "goal": "买家2+改写，水印依然存活、溯源依然命中。",
    },
]

_BY_ID = {c["case_id"]: c for c in CASES}


def list_cases() -> list[dict]:
    return CASES


def get_case(case_id: str) -> dict:
    if case_id not in _BY_ID:
        raise KeyError(f"未知案例: {case_id}")
    return _BY_ID[case_id]
