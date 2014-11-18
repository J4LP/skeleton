"""empty message

Revision ID: 21632321b09c
Revises: None
Create Date: 2014-11-18 14:53:55.266463

"""

# revision identifiers, used by Alembic.
revision = '21632321b09c'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import IPAddressType, ArrowType


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('main_character', sa.String(), nullable=True),
    sa.Column('main_character_id', sa.Integer(), nullable=True),
    sa.Column('alliance_name', sa.String(), nullable=True),
    sa.Column('corporation_name', sa.String(), nullable=True),
    sa.Column('last_ip', IPAddressType(length=50), nullable=True),
    sa.Column('last_login_on', ArrowType(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###