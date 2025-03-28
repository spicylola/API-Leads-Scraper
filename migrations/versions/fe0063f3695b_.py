"""empty message

Revision ID: fe0063f3695b
Revises: 
Create Date: 2025-03-18 15:14:16.478872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe0063f3695b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('businesses',
    sa.Column('place_id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('modified_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('display_name', sa.String(), nullable=False),
    sa.Column('current_opening_hours', sa.Text(), nullable=True),
    sa.Column('website_uri', sa.String(), nullable=True),
    sa.Column('formatted_address', sa.String(), nullable=False),
    sa.Column('google_maps_uri', sa.String(), nullable=False),
    sa.Column('national_phone_number', sa.String(), nullable=True),
    sa.Column('business_type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('place_id'),
    sa.UniqueConstraint('place_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('modified_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('excel_requests',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('request_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('error_msg', sa.String(), nullable=True),
    sa.Column('file_path', sa.Text(), nullable=True),
    sa.Column('download_url', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('request_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('excel_requests')
    op.drop_table('users')
    op.drop_table('businesses')
    # ### end Alembic commands ###
