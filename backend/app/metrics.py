"""实验指标总览（⑤ 实验指标总览页）。

这些是“整体可信度”数字，用于证明方法不是个例，前端直接渲染对比图表。
"""
from __future__ import annotations

OWNER_VERIFICATION = {
    "title": "所有权验证",
    "metrics": [
        {"name": "准确率 Accuracy", "ours": 0.992, "promptcare": 0.896, "promptcos": 0.875,
         "higher_is_better": True},
        {"name": "True-WS", "ours": 0.992, "promptcare": 0.832, "promptcos": 0.865,
         "higher_is_better": True},
        {"name": "False-WS", "ours": 0.037, "promptcare": 0.097, "promptcos": 0.174,
         "higher_is_better": False},
        {"name": "Margin", "ours": 0.956, "promptcare": 0.735, "promptcos": 0.691,
         "higher_is_better": True},
    ],
    "takeaway": "本方法平均所有权验证准确率 99.2%，Margin 0.956，全面优于两个 prompt 级基线。",
}

BUYER_ATTRIBUTION = {
    "title": "泄露源定位（Top-1）",
    "metrics": [
        {"name": "Top-1 准确率", "ours": 0.993, "promptcare": 0.705, "promptcos": 0.676,
         "higher_is_better": True},
    ],
    "takeaway": "授权副本持有方 Top-1 溯源准确率 99.3%，远高于基线（70.5% / 67.6%），"
                "说明词槽候选词编码携带了足够的授权副本专属信息。",
}

ROBUSTNESS = {
    "title": "鲁棒性（四类盲攻击下的授权副本持有方 Top-1）",
    "metrics": [
        {"name": "改写 Paraphrase", "buyer_top1": 0.976, "owner_acc": 0.998},
        {"name": "压缩 Compression", "buyer_top1": 0.996, "owner_acc": 0.999},
        {"name": "辅助条款删除 Aux deletion", "buyer_top1": 0.910, "owner_acc": 0.995},
        {"name": "章节重排 Reorganization", "buyer_top1": 0.998, "owner_acc": 0.998},
    ],
    "takeaway": "四类攻击下所有权验证均≥99.5%；最难的辅助条款删除授权副本持有方 Top-1 仍≥91%。"
                "（与演示页对应：第一类攻击 = 改写 / 压缩 / 章节重排，第二类攻击 = 辅助条款删除。）",
}

FIDELITY = {
    "title": "保真度（加水印是否影响正常功能）",
    "metrics": [
        {"name": "效用下降 Utility Drop（任务评分绝对降幅，非百分比；越低越好）", "ours": 0.662,
         "promptcare": 0.700, "higher_is_better": False},
        {"name": "语义一致性 Semantic Consistency", "ours": 0.727,
         "promptcare": 0.559, "higher_is_better": True},
    ],
    "takeaway": "注：Utility Drop 衡量加水印前后任务评分的绝对降幅（评分量纲下的差值，不是“下降 66.2%”）。"
                "本方法降幅低于基线 PromptCARE，语义一致性显著更高，正常使用基本不受影响。",
}

ABLATION = {
    "title": "消融实验（每个设计是否真的必要）",
    "items": [
        {"remove": "去掉隐式审计支路", "effect": "SAR 主载体缺失，确权与定位同时崩溃"},
        {"remove": "去掉缺项对照查询", "effect": "缺少对照会削弱码位恢复稳定性"},
        {"remove": "去掉授权副本纠错码", "effect": "无法进行授权对象区分"},
        {"remove": "去掉词槽候选词表", "effect": "自由文本无法稳定还原比特"},
        {"remove": "去掉攻击质量筛选", "effect": "对抗场景下可解码性下降"},
        {"remove": "去掉验证示例", "effect": "示例对 SAR 稳定触发十分关键"},
    ],
    "takeaway": "去掉任一核心组件性能都明显下降，证明每个设计都是必要的，而非摆设。",
}


def _run_official() -> dict | None:
    """读取本次真实运行（GPT-5 mini + LangChain）的官方逐域指标，作为“本场实测”板块。"""
    from . import config, data_access
    if not config.EVIDENCE_AVAILABLE:
        return None

    def rows_of(name):
        d = data_access.load_evidence_result(name)
        return (d or {}).get("rows", []) if d else []

    return {
        "run_tag": config.EVIDENCE_RUN,
        "model": config.EVIDENCE_MODEL,
        "agent": config.EVIDENCE_AGENT,
        "effectiveness_distinctiveness": rows_of("effectiveness_distinctiveness"),
        "buyer_attribution": rows_of("buyer_attribution"),
        "robustness": rows_of("robustness"),
        "fidelity": rows_of("fidelity"),
        "note": "以上为本次展示所用真实运行的官方指标（按域/攻击列出），与整体汇总方向一致。",
    }


def overview() -> dict:
    return {
        "overall": {
            "owner_verification": OWNER_VERIFICATION,
            "buyer_attribution": BUYER_ATTRIBUTION,
            "robustness": ROBUSTNESS,
            "fidelity": FIDELITY,
            "ablation": ABLATION,
            "source": "三域泛化实验汇总指标",
        },
        "run_official": _run_official(),
    }
