"""use new models Page and Useraa

Revision ID: 00913effe72f
Revises: 21b3b82736c3
Create Date: 2020-07-26 22:36:29.743261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00913effe72f'
down_revision = '21b3b82736c3'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('data', sa.Text(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], name=op.f('fk_pages_creator_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_pages')),
    sa.UniqueConstraint('name', name=op.f('uq_pages_name'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pages')
    # ### end Alembic commands ###
