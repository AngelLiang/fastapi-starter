from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime,
    Float, ForeignKey, Index, Integer, String, Table, Text,
    text
)
# from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, UUID, ARRAY
from sqlalchemy.orm import relationship

from .database import Base

# from sqlalchemy.ext.declarative import declarative_base

metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        {'comment': '用户表'}
    )

    id = Column(BigInteger, primary_key=True, comment='主键')
    uid = Column(String(32), unique=True, comment='uid')
    openid = Column(String(255), unique=True, index=True, comment='微信openid')
    nickname = Column(String(255), nullable=False, comment='用户昵称')
    phone = Column(String(255), nullable=False, unique=True, comment='手机号')
    password_hash = Column(String(255), nullable=False, comment='密码哈希')
    role = Column(String(255), nullable=False, comment='角色。默认是user', default='uesr')
    avatar = Column(String(255), comment='头像')
    created_at = Column(DateTime(True), nullable=False, comment='创建时间')
    updated_at = Column(DateTime(True), nullable=False, comment='更新时间')
