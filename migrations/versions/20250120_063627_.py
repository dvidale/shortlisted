"""empty message

Revision ID: f3c83673193a
Revises: 5641b4195f58
Create Date: 2025-01-20 06:36:27.084491

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = 'f3c83673193a'
down_revision = '5641b4195f58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # if environment == "production":
    #     with op.batch_alter_table('users', schema={SCHEMA}) as batch_op:
    #         batch_op.alter_column('hasMessages',
    #             existing_type=sa.BOOLEAN(),
    #             type_=sa.Integer(),
    #             existing_nullable=True,
    #             existing_server_default=sa.text("'False'"),
    #             postgresql_using='hasMessages::integer')
    # else:
    #     with op.batch_alter_table('users', schema=None) as batch_op:
    #         batch_op.alter_column('hasMessages',
    #             existing_type=sa.BOOLEAN(),
    #             type_=sa.Integer(),
    #             existing_nullable=True,
    #             existing_server_default=sa.text("'False'"))
    pass

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # if environment == "production":
    #     with op.batch_alter_table('users', schema={SCHEMA}) as batch_op:
    #         batch_op.alter_column('hasMessages',
    #             existing_type=sa.Integer(),
    #             type_=sa.BOOLEAN(),
    #             existing_nullable=True,
    #             existing_server_default=sa.text("'False'"),
    #             postgresql_using='hasMessages::integer')
    # else:
    #     with op.batch_alter_table('users', schema=None) as batch_op:
    #         batch_op.alter_column('hasMessages',
    #             existing_type=sa.Integer(),
    #             type_=sa.BOOLEAN(),
    #             existing_nullable=True,
    #             existing_server_default=sa.text("'False'"))
    pass

    # ### end Alembic commands ###
