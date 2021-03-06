"""empty message

Revision ID: 3723b6b6851d
Revises: 
Create Date: 2018-07-13 02:20:13.523275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3723b6b6851d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(length=10), nullable=False),
    sa.Column('password', sa.String(length=15), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('daftar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=30), nullable=False),
    sa.Column('ttl', sa.String(length=60), nullable=False),
    sa.Column('jenis_kelamin', sa.String(length=30), nullable=False),
    sa.Column('agama', sa.String(length=10), nullable=False),
    sa.Column('status', sa.String(length=15), nullable=False),
    sa.Column('no_telpon', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=25), nullable=False),
    sa.Column('alamat', sa.String(length=30), nullable=False),
    sa.Column('prodi', sa.String(length=20), nullable=False),
    sa.Column('sekolah_asal', sa.String(length=20), nullable=False),
    sa.Column('alamat_sekolah', sa.String(length=20), nullable=False),
    sa.Column('thn_lulus', sa.Integer(), nullable=False),
    sa.Column('jurusan', sa.String(length=20), nullable=False),
    sa.Column('nilairata', sa.String(length=7), nullable=False),
    sa.Column('no_ijazah', sa.String(length=50), nullable=False),
    sa.Column('nama_wali', sa.String(length=20), nullable=False),
    sa.Column('profesi', sa.String(length=20), nullable=False),
    sa.Column('alamat_wali', sa.String(length=60), nullable=False),
    sa.Column('pendidikan', sa.String(length=10), nullable=False),
    sa.Column('no_hp', sa.String(length=15), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daftar')
    op.drop_table('admin')
    # ### end Alembic commands ###
