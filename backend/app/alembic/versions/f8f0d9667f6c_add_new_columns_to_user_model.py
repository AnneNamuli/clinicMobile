"""Add new columns to user model

Revision ID: f8f0d9667f6c
Revises: d4867f3a4c0a
Create Date: 2021-06-04 10:13:27.058110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8f0d9667f6c'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(), nullable=True))
    op.add_column('user', sa.Column('phone_number', sa.String(), nullable=True))
    op.add_column('user', sa.Column('id_number', sa.String(), nullable=True))
    op.add_column('user', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('user', sa.Column('role', sa.String(), nullable=True))
    op.add_column('user', sa.Column('date_of_birth', sa.Date(), nullable=True))
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_index(op.f('ix_user_id_number'), 'user', ['id_number'], unique=True)
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.drop_index(op.f('ix_user_id_number'), table_name='user')
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('user', 'created_at')
    op.drop_column('user', 'date_of_birth')
    op.drop_column('user', 'role')
    op.drop_column('user', 'gender')
    op.drop_column('user', 'id_number')
    op.drop_column('user', 'phone_number')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###
