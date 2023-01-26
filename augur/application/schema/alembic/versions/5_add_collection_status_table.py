"""Add collection status table

Revision ID: 5
Revises: 4
Create Date: 2023-01-26 08:30:05.524959

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5'
down_revision = '4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collection_status',
    sa.Column('repo_id', sa.BigInteger(), nullable=False),
    sa.Column('data_last_collected', postgresql.TIMESTAMP(), nullable=True),
    sa.Column('event_last_collected', postgresql.TIMESTAMP(), nullable=True),
    sa.Column('status', sa.String(), server_default=sa.text("'Pending'"), nullable=False),
    sa.Column('task_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['repo_id'], ['augur_data.repo.repo_id'], name='collection_status_repo_id_fk'),
    sa.PrimaryKeyConstraint('repo_id'),
    schema='augur_operations'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collection_status', schema='augur_operations')
    # ### end Alembic commands ###
