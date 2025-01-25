"""empty message

Revision ID: de94f245778f
Revises: 3cf24561cd8f
Create Date: 2025-01-20 09:05:33.491921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de94f245778f'
down_revision = '3cf24561cd8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('receivedMsgs', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('receivedMsgs')

    # ### end Alembic commands ###
