"""add basic user table

Revision ID: 9461f68da2b8
Revises: None
Create Date: 2023-02-01 17:55:53.705414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9461f68da2b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forum_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_forum_users_id'), 'forum_users', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_forum_users_id'), table_name='forum_users')
    op.drop_table('forum_users')
    # ### end Alembic commands ###
