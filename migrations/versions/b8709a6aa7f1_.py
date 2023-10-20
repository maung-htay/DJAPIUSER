"""empty message

Revision ID: b8709a6aa7f1
Revises: 
Create Date: 2023-10-18 22:22:22.389839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8709a6aa7f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('street', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('countries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('role', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('authors')
    op.drop_table('users')
    op.drop_table('stores')
    op.drop_table('countries')
    op.drop_table('address')
    # ### end Alembic commands ###
