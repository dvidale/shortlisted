from flask.cli import AppGroup
from app.models.db import db, environment, SCHEMA

from .users import seed_users, undo_users
from .job_titles import seed_job_titles,undo_job_titles
from .industry_areas import seed_industry_areas, undo_industry_areas
from .genres import seed_genres,undo_genres
from .locations import seed_locations, undo_locations

from .user_job_titles import seed_user_job_titles, undo_user_job_titles
from .user_industries import seed_user_industries, undo_user_industries
from .user_genres import seed_user_genres, undo_user_genres
from .user_locations import seed_user_locations, undo_user_locations




# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_user_locations()
        undo_user_genres()
        undo_user_industries()
        undo_user_job_titles()
        undo_locations()
        undo_genres()
        undo_industry_areas()
        undo_job_titles()
        undo_users()
    seed_users()
    seed_job_titles()
    seed_industry_areas()
    seed_genres()
    seed_locations()
    seed_user_job_titles()
    seed_user_industries()
    seed_user_genres()
    seed_user_locations()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_user_locations()
    undo_user_genres()
    undo_user_industries()
    undo_user_job_titles()
    undo_locations()
    undo_genres()
    undo_industry_areas()
    undo_job_titles()
    undo_users()
    # Add other undo functions here
