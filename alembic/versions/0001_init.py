"""init

Revision ID: 0001
Revises: 
Create Date: 2025-02-22 15:21:50.014618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False, comment='主键'),
    sa.Column('uid', sa.String(length=32), nullable=True, comment='uid'),
    sa.Column('openid', sa.String(length=255), nullable=True, comment='微信openid'),
    sa.Column('nickname', sa.String(length=255), nullable=False, comment='用户昵称'),
    sa.Column('phone', sa.String(length=255), nullable=False, comment='手机号'),
    sa.Column('password_hash', sa.String(length=255), nullable=False, comment='密码哈希'),
    sa.Column('role', sa.String(length=255), nullable=False, comment='角色。默认是user'),
    sa.Column('avatar', sa.String(length=255), nullable=True, comment='头像'),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, comment='创建时间'),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, comment='更新时间'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('uid'),
    comment='用户表'
    )
    op.create_index(op.f('ix_user_openid'), 'user', ['openid'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_openid'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
