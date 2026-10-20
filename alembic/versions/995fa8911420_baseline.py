"""baseline

Revision ID: 995fa8911420
Revises:
Create Date: 2026-10-20 23:13:03.152986

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "995fa8911420"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
