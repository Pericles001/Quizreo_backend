"""generated applications models

Revision ID: ebf9e49bcad9
Revises: 6385841db998
Create Date: 2022-09-11 02:17:35.786122

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ebf9e49bcad9'
down_revision = '6385841db998'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_roles', sa.ARRAY(sa.Enum('Administrator', 'Simple User', name='userrole', native_enum=False)), nullable=True))
    op.drop_column('users', 'user_types')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_types', postgresql.ARRAY(sa.VARCHAR(length=13)), autoincrement=False, nullable=True))
    op.drop_column('users', 'user_roles')
    # ### end Alembic commands ###
