#!/usr/bin/env python3
"""Read-only structure checks and request-routing smoke tests for Career Application OS."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


DEFAULT_VAULT = Path(os.environ.get("CAREER_OS_VAULT", str(Path.cwd() / "Career-OS"))).expanduser()
DEFAULT_ASU = Path(os.environ["ASU_SKILLS_SOURCE"]).expanduser() if os.environ.get("ASU_SKILLS_SOURCE") else None
DEFAULT_TAILOR = Path(os.environ["TAILOR_SKILL_SOURCE"]).expanduser() if os.environ.get("TAILOR_SKILL_SOURCE") else None
DEFAULT_SKILLS = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser() / "skills"

VALID_EVIDENCE_STATUSES = {"VERIFIED", "REFRAMED", "INFERRED", "PROJECT_TO_COMPLETE"}
ASU_SKILLS = {
    "contributor",
    "evidence-recap",
    "project-guide",
    "great-resume",
    "make-resume",
    "job-match",
    "job-apply",
    "interview",
    "offer",
}

APPLICATION_INTENT_TERMS = (
    "我要投",
    "申请这个",
    "投这个",
    "准备投",
    "apply to",
    "job application",
)
FIT_ONLY_TERMS = (
    "只分析",
    "先分析",
    "只想知道适不适合",
    "帮我看看这个岗位适不适合我",
    "看看这个岗位适不适合我",
    "适不适合我",
    "only analyze",
    "analysis only",
    "fit only",
)
RESEARCH_ONLY_TERMS = (
    "只研究",
    "research only",
    "only research",
)
EXPLORE_ONLY_TERMS = (
    "只探索",
    "只是看看",
    "不准备投",
    "不打算投",
    "暂时不投",
    "explore only",
    "only explore",
)
COMPARE_ONLY_TERMS = (
    "只比较",
    "compare only",
    "only compare",
)
NO_RESUME_TERMS = (
    "不要做简历",
    "不用做简历",
    "先不要做简历",
    "不需要简历",
    "do not create a resume",
    "don't create a resume",
    "no resume",
)
RESPONSIBILITY_HEADINGS = (
    "岗位职责",
    "职位职责",
    "工作职责",
    "职责描述",
    "responsibilities",
    "job duties",
    "what you'll do",
    "what you will do",
)
REQUIREMENT_HEADINGS = (
    "任职要求",
    "职位要求",
    "岗位要求",
    "任职资格",
    "招聘要求",
    "requirements",
    "qualifications",
    "what we're looking for",
    "what we are looking for",
)


def contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def is_recognizable_jd(text: str) -> bool:
    explicit_full_jd = contains_any(text, ("完整jd", "完整 jd", "complete jd", "full jd"))
    has_responsibilities = contains_any(text, RESPONSIBILITY_HEADINGS)
    has_requirements = contains_any(text, REQUIREMENT_HEADINGS)
    structured_jd = (
        len(text) >= 250
        and contains_any(text, ("职位详情", "职位描述", "job description", "role description"))
        and (has_responsibilities or has_requirements)
    )
    return explicit_full_jd or (has_responsibilities and has_requirements) or structured_jd


def explicit_jd_scope_limit(text: str) -> str | None:
    if contains_any(text, COMPARE_ONLY_TERMS):
        return "COMPARE_ROLES"
    if contains_any(text, RESEARCH_ONLY_TERMS) or (
        contains_any(text, NO_RESUME_TERMS)
        and contains_any(text, ("研究", "research"))
    ):
        return "RESEARCH_COMPANY_ROLE"
    if contains_any(text, FIT_ONLY_TERMS):
        return "FIT_ANALYSIS"
    if contains_any(text, EXPLORE_ONLY_TERMS):
        return "EXPLORE_ROLE"
    if contains_any(text, NO_RESUME_TERMS):
        return "FIT_ANALYSIS"
    return None


def route_request(text: str) -> str:
    normalized = re.sub(r"\s+", " ", text.strip().lower())
    if is_recognizable_jd(normalized):
        scope_limit = explicit_jd_scope_limit(normalized)
        return scope_limit or "APPLICATION"
    if any(term in normalized for term in ("面试", "interview")):
        return "INTERVIEW"
    if contains_any(normalized, APPLICATION_INTENT_TERMS):
        return "APPLICATION"
    if "jd" in normalized and any(term in normalized for term in ("投", "申请", "resume", "简历")):
        return "APPLICATION"
    if any(term in normalized for term in ("比较", "对比", "compare")):
        return "COMPARE_ROLES"
    if any(term in normalized for term in ("体验", "现实测试", "reality test", "experiment")):
        return "CAREER_EXPERIMENT"
    if contains_any(normalized, FIT_ONLY_TERMS) or any(
        term in normalized for term in ("适不适合", "匹配", "fit analysis", "适配")
    ):
        return "FIT_ANALYSIS"
    if any(term in normalized for term in ("研究", "公司", "company")):
        return "RESEARCH_COMPANY_ROLE"
    return "EXPLORE_ROLE"


def require(path: Path, label: str, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"missing {label}: {path}")


def frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    return parts[1] if len(parts) == 3 else ""


def doctor(vault: Path, asu: Path | None, tailor: Path | None, skills: Path) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    required_vault_dirs = [
        "00_Home",
        "01_My_Evidence",
        "02_Roles",
        "03_Companies",
        "04_Applications",
        "05_Career_Experiments",
        "06_Templates",
        "07_Resumes",
        "99_Raw",
    ]
    required_home = [
        "Career Dashboard.md",
        "My Profile.md",
        "Personal Evidence Intake.md",
        "Career Map.md",
        "Evidence Index.md",
        "Role Index.md",
        "Company Index.md",
        "Application Index.md",
    ]
    for item in required_vault_dirs:
        require(vault / item, f"Vault directory {item}", errors)
    for item in required_home:
        require(vault / "00_Home" / item, f"home file {item}", errors)

    if asu is not None:
        require(asu, "configured ASu source", errors)
    if tailor is not None:
        require(tailor, "configured Tailor source", errors)
    for name in sorted(ASU_SKILLS):
        if not (skills / name / "SKILL.md").exists():
            warnings.append(f"optional integration unavailable: {name}")
    if not (skills / "tailor-job-application" / "SKILL.md").exists():
        warnings.append("optional integration unavailable: tailor-job-application")
    require(Path(__file__).resolve().parents[1] / "SKILL.md", "main skill", errors)

    evidence_root = vault / "01_My_Evidence"
    if evidence_root.exists():
        for note in evidence_root.rglob("*.md"):
            text = note.read_text(encoding="utf-8")
            fm = frontmatter(text)
            id_match = re.search(r"(?m)^id:\s*(\S+)", fm)
            status_match = re.search(r"(?m)^status:\s*(\S+)", fm)
            if id_match and (not status_match or status_match.group(1) not in VALID_EVIDENCE_STATUSES):
                errors.append(f"invalid evidence status: {note}")
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if errors:
        return 1
    print("Career OS structure is valid")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor_parser = subparsers.add_parser("doctor", help="validate the installed system")
    doctor_parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    doctor_parser.add_argument("--asu", type=Path, default=DEFAULT_ASU)
    doctor_parser.add_argument("--tailor", type=Path, default=DEFAULT_TAILOR)
    doctor_parser.add_argument("--skills", type=Path, default=DEFAULT_SKILLS)

    route_parser = subparsers.add_parser("route", help="classify one request")
    route_parser.add_argument("text")

    args = parser.parse_args()
    if args.command == "route":
        print(route_request(args.text))
        return 0
    return doctor(args.vault, args.asu, args.tailor, args.skills)


if __name__ == "__main__":
    sys.exit(main())
