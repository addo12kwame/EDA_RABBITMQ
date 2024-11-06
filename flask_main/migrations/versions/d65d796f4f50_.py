"""empty message

Revision ID: d65d796f4f50
Revises: 345cda27cfb7
Create Date: 2024-11-06 08:06:19.519420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd65d796f4f50'
down_revision = '345cda27cfb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['user_id'])
        batch_op.create_unique_constraint(None, ['product_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###