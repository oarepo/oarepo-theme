#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-theme (see https://github.com/oarepo/oarepo-theme).
#
# oarepo-theme is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
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
