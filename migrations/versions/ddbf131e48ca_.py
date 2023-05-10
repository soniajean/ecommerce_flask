"""empty message

Revision ID: ddbf131e48ca
Revises: 3471d8f9086c
Create Date: 2023-05-10 12:47:49.606137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddbf131e48ca'
down_revision = '3471d8f9086c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_plan',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_table('my_cart')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_cart',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('exercise_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], name='my_cart_exercise_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='my_cart_user_id_fkey')
    )
    op.drop_table('my_plan')
    # ### end Alembic commands ###
