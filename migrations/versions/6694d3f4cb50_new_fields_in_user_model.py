"""new fields in user model

Revision ID: 6694d3f4cb50
Revises: d8a5d5c4d09f
Create Date: 2023-04-04 09:12:48.455369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6694d3f4cb50'
down_revision = 'd8a5d5c4d09f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
