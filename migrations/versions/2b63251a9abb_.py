"""empty message

Revision ID: 2b63251a9abb
Revises: 4306febfb0e6
Create Date: 2022-10-11 22:00:12.414144

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2b63251a9abb'
down_revision = '4306febfb0e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_post', 'likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('likes', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
