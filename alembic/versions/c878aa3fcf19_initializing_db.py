"""Initializing DB

Revision ID: c878aa3fcf19
Revises:
Create Date: 2022-09-01 15:42:49.639335

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c878aa3fcf19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('sp100Prices')
    # ### end Alembic commands ###
    pass


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('sp100Prices',
    # sa.Column('date', mysql.VARCHAR(length=252), nullable=False),
    # sa.Column('symbol', mysql.VARCHAR(length=252), nullable=False),
    # sa.Column('price', mysql.FLOAT(), nullable=False),
    # sa.PrimaryKeyConstraint('date', 'symbol', 'price'),
    # mysql_collate='utf8mb4_0900_ai_ci',
    # mysql_default_charset='utf8mb4',
    # mysql_engine='InnoDB'
    # )
    # # ### end Alembic commands ###
    pass
