"""last_updated_at added to user model

Revision ID: 6b86277f53c0
Revises: f8f0d9667f6c
Create Date: 2021-06-04 10:24:32.418363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b86277f53c0'
down_revision = 'f8f0d9667f6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_updated_at')
    # ### end Alembic commands ###
