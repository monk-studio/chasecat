"""init

Revision ID: 180ee7f44e0c
Revises:
Create Date: 2018-04-19 21:31:14.292280

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '180ee7f44e0c'
down_revision = None
branch_labels = ('default',)
depends_on = None


def upgrade():
    op.create_table(
        'leaderboard',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.String(length=100),
                  nullable=False),
        sa.Column('user_name', sa.String(length=20),
                  nullable=False),
        sa.Column('score', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id')
    )


def downgrade():
    op.drop_table('leaderboard')
