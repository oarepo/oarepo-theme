# SPDX-FileCopyrightText: 2025 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

from __future__ import annotations

import pytest
from invenio_app.factory import create_ui as _create_ui


@pytest.fixture(scope="module")
def ui_app(request, app_config):
    """UI Application fixture."""
    app = _create_ui()
    app.config.update(app_config)
    return app
