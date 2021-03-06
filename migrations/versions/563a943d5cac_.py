"""empty message

Revision ID: 563a943d5cac
Revises: a307a5ddeb84
Create Date: 2021-03-12 16:43:55.460401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '563a943d5cac'
down_revision = 'a307a5ddeb84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
