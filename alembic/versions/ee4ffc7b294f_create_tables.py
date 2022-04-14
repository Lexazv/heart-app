"""create tables

Revision ID: ee4ffc7b294f
Revises: 
Create Date: 2022-03-29 19:14:03.943242

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee4ffc7b294f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),  
        sa.Column('email', sa.String(255), unique=True),
        sa.Column('password', sa.String(500)),
        sa.Column('first_name', sa.String(255), nullable=True),
        sa.Column('last_name', sa.String(255), nullable=True),
        sa.Column('created_on', sa.DateTime, default=datetime.now())
    )

    op.create_table(
        'file_data',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('filename', sa.String(255)),
        sa.Column('extention', sa.String(10)),
        sa.Column('created_on', sa.DateTime, default=datetime.now())
    )

    op.create_table(
        'heart_data',
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


def downgrade():
    table_names = ['heart_data', 'file_data', 'user']

    for name in table_names:
        op.drop_table(name)
