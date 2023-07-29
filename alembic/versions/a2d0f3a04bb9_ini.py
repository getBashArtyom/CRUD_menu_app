"""ini

Revision ID: a2d0f3a04bb9
Revises: 8f890a9c630f
Create Date: 2023-07-29 12:35:24.632855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2d0f3a04bb9'
down_revision = '8f890a9c630f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'menus',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('title', sa.String(length=255), nullable=False, unique=True),
        sa.Column('description', sa.String(length=255), nullable=False),
    )

    op.create_table(
        'submenus',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('title', sa.String(length=255), nullable=False, unique=True),
        sa.Column('description', sa.String(length=255), nullable=False),
        sa.Column('menu_id', sa.String(length=36), sa.ForeignKey('menus.id'), nullable=False),
    )

    op.create_table(
        'dishes',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('title', sa.String(length=255), nullable=False, unique=True),
        sa.Column('description', sa.String(length=255), nullable=False),
        sa.Column('price', sa.Float(precision=2), nullable=True),
        sa.Column('submenu_id', sa.String(length=36), sa.ForeignKey('submenus.id'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('dishes')

    op.drop_table('submenus')

    op.drop_table('menus')
