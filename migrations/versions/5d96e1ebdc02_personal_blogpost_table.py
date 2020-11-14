"""personal blogpost table

Revision ID: 5d96e1ebdc02
Revises: 2737f391a682
Create Date: 2020-11-14 13:57:58.949987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d96e1ebdc02'
down_revision = '2737f391a682'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personal_blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=500), nullable=True),
    sa.Column('body_html', sa.String(length=500), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_personal_blog_post_timestamp'), 'personal_blog_post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_personal_blog_post_timestamp'), table_name='personal_blog_post')
    op.drop_table('personal_blog_post')
    # ### end Alembic commands ###
