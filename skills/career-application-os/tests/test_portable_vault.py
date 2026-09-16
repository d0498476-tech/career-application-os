from __future__ import annotations

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def load_module(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


INIT = load_module("init_vault")
CHECK = load_module("check_career_os")


class PortableVaultTests(unittest.TestCase):
    def test_blank_vault_passes_without_integrations(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            vault = root / "Career-OS"
            INIT.initialize(vault)
            with contextlib.redirect_stdout(io.StringIO()):
                result = CHECK.doctor(vault, None, None, root / "missing-optional-skills")
            self.assertEqual(result, 0)

    def test_existing_profile_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            vault = Path(temp) / "Career-OS"
            INIT.initialize(vault)
            profile = vault / "00_Home" / "My Profile.md"
            sentinel = "Preserve the user's existing content\n"
            profile.write_text(sentinel, encoding="utf-8")
            self.assertEqual(INIT.initialize(vault), [])
            self.assertEqual(profile.read_text(encoding="utf-8"), sentinel)

    def test_invalid_evidence_status_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            vault = root / "Career-OS"
            INIT.initialize(vault)
            (vault / "01_My_Evidence" / "invalid.md").write_text(
                "---\nid: EXP-TEST\nstatus: UNKNOWN\n---\n", encoding="utf-8"
            )
            with contextlib.redirect_stdout(io.StringIO()):
                result = CHECK.doctor(vault, None, None, root / "missing-optional-skills")
            self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
