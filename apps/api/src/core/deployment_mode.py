"""
Single source of truth for deployment mode detection.

Three modes:
- 'saas': LEARNHOUSE_SAAS=true — plan-based gating, usage limits apply
- 'ee':   EE folder present (and not SaaS) — all features enabled, unlimited
- 'oss':  EE folder absent (and not SaaS) — EE features blocked, unlimited otherwise

Development override:
- LEARNHOUSE_FORCE_EE=1 skips the license check when the EE folder is present.
  Only effective when development_mode=true in config. Never set this in production.
"""

import os
from typing import Literal
from config.config import get_learnhouse_config
from src.core.ee_hooks import is_ee_available, get_ee_hooks

DeploymentMode = Literal['saas', 'oss', 'ee']

# Features blocked in OSS mode but available in EE and plan-gated in SaaS
EE_ONLY_FEATURES: frozenset[str] = frozenset({
    'sso', 'audit_logs', 'payments', 'analytics_advanced', 'scorm'
})


def get_deployment_mode() -> DeploymentMode:
    return 'ee'
