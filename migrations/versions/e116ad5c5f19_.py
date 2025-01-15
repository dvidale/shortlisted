"""empty message

Revision ID: e116ad5c5f19
Revises: b19e6e749cdf
Create Date: 2025-01-14 21:03:29.376903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e116ad5c5f19'
down_revision = 'b19e6e749cdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('hasMessages')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hasMessages', sa.BOOLEAN(), nullable=True))

    # ### end Alembic commands ###
