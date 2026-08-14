# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""OARepo theme package initialization.

This package provides a Semantic UI theme overlay for InvenioRDM based
NRP repositories.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("oarepo-theme")
except PackageNotFoundError:
    __version__ = "0.0.0dev0+unknown"

__all__ = [
    "__version__",
]
