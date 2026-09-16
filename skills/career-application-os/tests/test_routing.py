from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_career_os.py"
SPEC = importlib.util.spec_from_file_location("check_career_os", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


JD = """
产品经理
岗位职责：
1. 分析区域市场机会并拆解需求。
2. 联合研发推动产品落地。
任职要求：
1. 本科及以上学历。
2. 具备数据分析能力。
"""


class DefaultJdRoutingTests(unittest.TestCase):
    def test_case_1_full_jd_defaults_to_application(self) -> None:
        self.assertEqual(MODULE.route_request(JD), "APPLICATION")

    def test_case_2_fit_only_with_jd(self) -> None:
        request = "帮我看看这个岗位适不适合我\n" + JD
        self.assertEqual(MODULE.route_request(request), "FIT_ANALYSIS")

    def test_case_3_research_without_resume(self) -> None:
        request = "研究这个岗位，不要做简历"
        self.assertEqual(MODULE.route_request(request), "RESEARCH_COMPANY_ROLE")

    def test_case_4_explicit_application_with_jd(self) -> None:
        request = "我要投这个岗位\n" + JD
        self.assertEqual(MODULE.route_request(request), "APPLICATION")

    def test_browse_only_with_jd(self) -> None:
        self.assertEqual(MODULE.route_request("只是看看，不准备投\n" + JD), "EXPLORE_ROLE")

    def test_research_only_with_jd(self) -> None:
        self.assertEqual(
            MODULE.route_request("研究这个岗位，不要做简历\n" + JD),
            "RESEARCH_COMPANY_ROLE",
        )

    def test_english_complete_jd_defaults_to_application(self) -> None:
        english_jd = "Responsibilities: analyze regional demand. Qualifications: bachelor's degree."
        self.assertEqual(MODULE.route_request(english_jd), "APPLICATION")

    def test_explore_only_with_english_jd(self) -> None:
        english_jd = "explore only. Responsibilities: analyze demand. Requirements: bachelor's degree."
        self.assertEqual(MODULE.route_request(english_jd), "EXPLORE_ROLE")


if __name__ == "__main__":
    unittest.main()
