"""empty message

Revision ID: 9eed42c1c666
Revises: 3723b6b6851d
Create Date: 2018-07-15 05:09:09.677727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9eed42c1c666'
down_revision = '3723b6b6851d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admin', 'password_hash')
    # ### end Alembic commands ###
