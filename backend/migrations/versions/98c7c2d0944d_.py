"""empty message

Revision ID: 98c7c2d0944d
Revises: 
Create Date: 2020-06-17 15:11:43.255668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98c7c2d0944d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empresa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('region', sa.String(length=255), nullable=False),
    sa.Column('marketOpen', sa.String(length=255), nullable=False),
    sa.Column('marketClose', sa.String(length=255), nullable=False),
    sa.Column('timezone', sa.String(length=255), nullable=False),
    sa.Column('currency', sa.String(length=255), nullable=False),
    sa.Column('matchScore', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('idade', sa.String(length=255), nullable=False),
    sa.Column('profissao', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cotacao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=255), nullable=False),
    sa.Column('open', sa.String(length=255), nullable=False),
    sa.Column('high', sa.String(length=255), nullable=False),
    sa.Column('low', sa.String(length=255), nullable=False),
    sa.Column('close', sa.String(length=255), nullable=False),
    sa.Column('volume', sa.String(length=255), nullable=False),
    sa.Column('empresa_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['empresa_id'], ['empresa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cotacao')
    op.drop_table('usuario')
    op.drop_table('empresa')
    # ### end Alembic commands ###
