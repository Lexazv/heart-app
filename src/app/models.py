from datetime import datetime

import sqlalchemy as sa


metadata = sa.MetaData()


user = sa.Table(
    'user',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('email', sa.String(255), unique=True),
    sa.Column('password', sa.String(500)),
    sa.Column('first_name', sa.String(255)),
    sa.Column('last_name', sa.String(255)),
    sa.Column('created_on', sa.DateTime, default=datetime.now())
)


file_data = sa.Table(
    'file_data',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user', sa.Integer, sa.ForeignKey('user.id')),
    sa.Column('filename', sa.String(255)),
    sa.Column('extention', sa.String(10)),
    sa.Column('created_on', sa.DateTime, default=datetime.now())
)


heart_data = sa.Table(
    'heart_data',
    metadata,
    sa.Column('file', sa.Integer, sa.ForeignKey('file_data.id')),
    sa.Column('age', sa.Integer),
    sa.Column('sex', sa.Integer),
    sa.Column('cp', sa.Integer),
    sa.Column('trtbps', sa.Integer),
    sa.Column('chol', sa.Integer),
    sa.Column('fbs', sa.Integer),
    sa.Column('restecg', sa.Integer),
    sa.Column('thalachh', sa.Integer),
    sa.Column('exng', sa.Integer),
    sa.Column('oldpeak', sa.Float),
    sa.Column('slp', sa.Integer),
    sa.Column('caa', sa.Integer),
    sa.Column('thall', sa.Integer)
)
