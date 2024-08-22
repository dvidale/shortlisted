"""create all additional tables

Revision ID: 194aff989770
Revises: ffdc0a98111c
Create Date: 2024-08-21 23:50:34.800784

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")



# revision identifiers, used by Alembic.
revision = '194aff989770'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE genres SET SCHEMA {SCHEMA};")


    op.create_table('industry_areas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry_area', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE industry_areas SET SCHEMA {SCHEMA};")


    op.create_table('job_titles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE job_titles SET SCHEMA {SCHEMA};")


    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=50), nullable=True),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE locations SET SCHEMA {SCHEMA};")


    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=225), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('profile_img_url', sa.String(length=255), nullable=True),
    sa.Column('createdAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updatedAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")


    op.create_table('connections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('connected_id', sa.Integer(), nullable=True),
    sa.Column('connection_type', sa.String(length=50), nullable=False),
    sa.Column('connection_context', sa.String(length=100), nullable=False),
    sa.Column('createdAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updatedAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['connected_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE connections SET SCHEMA {SCHEMA};")


    op.create_table('shortlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('job_title_id', sa.Integer(), nullable=True),
    sa.Column('industry_area_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('optional_img', sa.String(length=255), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('createdAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updatedAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['created_by_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['industry_area_id'], ['industry_areas.id'], ),
    sa.ForeignKeyConstraint(['job_title_id'], ['job_titles.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE shortlists SET SCHEMA {SCHEMA};")

    op.create_table('user_genres',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )

    if environment == "production":
        op.execute(f"ALTER TABLE user_genres SET SCHEMA {SCHEMA};")


    op.create_table('user_industries',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('industry_area_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['industry_area_id'], ['industry_areas.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )

    if environment == "production":
        op.execute(f"ALTER TABLE user_industries SET SCHEMA {SCHEMA};")



    op.create_table('user_job_titles',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('job_title_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['job_title_id'], ['job_titles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'job_title_id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE user_job_titles SET SCHEMA {SCHEMA};")

    op.create_table('user_locations',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )

    if environment == "production":
        op.execute(f"ALTER TABLE user_locations SET SCHEMA {SCHEMA};")


    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('shortlist_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('createdAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updatedAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['shortlist_id'], ['shortlists.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE bookings SET SCHEMA {SCHEMA};")


    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shortlist_id', sa.Integer(), nullable=False),
    sa.Column('commenter_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('createdAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updatedAt', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['commenter_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['shortlist_id'], ['shortlists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE comments SET SCHEMA {SCHEMA};")



    op.create_table('referrals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shortlist_id', sa.Integer(), nullable=True),
    sa.Column('referrer_id', sa.Integer(), nullable=True),
    sa.Column('reffered_id', sa.Integer(), nullable=True),
    sa.Column('date_referred', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['referrer_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['reffered_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['shortlist_id'], ['shortlists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE referrals SET SCHEMA {SCHEMA};")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('referrals')
    op.drop_table('comments')
    op.drop_table('bookings')
    op.drop_table('user_locations')
    op.drop_table('user_job_titles')
    op.drop_table('user_industries')
    op.drop_table('user_genres')
    op.drop_table('shortlists')
    op.drop_table('connections')
    op.drop_table('users')
    op.drop_table('locations')
    op.drop_table('job_titles')
    op.drop_table('industry_areas')
    op.drop_table('genres')
    # ### end Alembic commands ###
