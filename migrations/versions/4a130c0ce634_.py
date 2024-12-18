"""empty message

Revision ID: 4a130c0ce634
Revises: 75563edc3c59
Create Date: 2024-10-27 17:18:42.524893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a130c0ce634'
down_revision = '75563edc3c59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('codes', schema=None) as batch_op:
        batch_op.drop_column('check_result')

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_column('testing_framework')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('testing_framework', sa.TEXT(), autoincrement=False, nullable=True))

    with op.batch_alter_table('codes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('check_result', sa.VARCHAR(length=255), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
