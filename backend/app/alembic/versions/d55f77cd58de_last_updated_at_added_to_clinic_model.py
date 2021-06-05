"""last_updated_at added to clinic model

Revision ID: d55f77cd58de
Revises: bc6395855f33
Create Date: 2021-06-04 17:40:39.524033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd55f77cd58de'
down_revision = 'bc6395855f33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clinic', sa.Column('contact_number', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'clinic', ['contact_number'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'clinic', type_='unique')
    op.drop_column('clinic', 'contact_number')
    # ### end Alembic commands ###