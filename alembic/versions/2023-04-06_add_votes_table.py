"""Add votes table

Revision ID: d3a52433344b
Revises: 8918b7a85e75
Create Date: 2023-04-06 22:00:02.522521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3a52433344b'
down_revision = '8918b7a85e75'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes_table',
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('post_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts_table.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user_table.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes_table')
    # ### end Alembic commands ###
