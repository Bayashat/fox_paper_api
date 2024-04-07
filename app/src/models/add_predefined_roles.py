"""Add predefined roles

Create Date: 2024-04-07  
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table


# Define the predefined roles
predefined_roles = [
    {'name': 'Admin'},
    {'name': 'Researcher'},
    {'name': 'User'}
]


def upgrade():
    # Create the role table
    op.create_table('role',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Insert predefined roles into the role table
    op.bulk_insert(table('role'), predefined_roles)


def downgrade():
    op.drop_table('role')
