"""Initial migration

Revision ID: 78e0f95dd6e8
Revises: e1f335d1f48e
Create Date: 2024-08-17 03:18:16.256666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78e0f95dd6e8'
down_revision: Union[str, None] = 'e1f335d1f48e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
