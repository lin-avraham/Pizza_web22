"""Add phone_number field to Order model

Revision ID: 0b225c79d47e
Revises: 
Create Date: 2024-06-24 22:45:26.091915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b225c79d47e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dish',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dish_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_name', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('order_details', sa.Text(), nullable=False),
    sa.Column('payment_method', sa.String(length=20), nullable=False),
    sa.Column('credit_card_number', sa.String(length=20), nullable=True),
    sa.Column('expiration_date', sa.String(length=10), nullable=True),
    sa.Column('cvv', sa.String(length=5), nullable=True),
    sa.Column('delivery_option', sa.String(length=20), nullable=False),
    sa.Column('delivery_address', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('user')
    op.drop_table('dish')
    # ### end Alembic commands ###
