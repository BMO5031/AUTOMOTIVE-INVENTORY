"""Add transaction_figure column

Revision ID: '20230907120000'  # Use a unique timestamp without dashes
Revises: '<previous_revision_id>'  # Replace with the actual previous revision ID
Create Date: 2023-09-07 12:00:00
"""
from alembic import op
import sqlalchemy as sa

revision = '20230907120000'  # Use a unique timestamp without dashes
down_revision = '<previous_revision_id>'  # Replace with the actual previous revision ID

def upgrade():
    op.add_column('transactions', sa.Column('transaction_figure', sa.Float()))

def downgrade():
    op.drop_column('transactions', 'transaction_figure')
