"""webdevelopment table

Revision ID: 665360d54256
Revises: 3620a4f06ce5
Create Date: 2020-11-14 17:02:04.705486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '665360d54256'
down_revision = '3620a4f06ce5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('web_development_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=500), nullable=True),
    sa.Column('body_html', sa.String(length=500), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_web_development_post_timestamp'), 'web_development_post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_web_development_post_timestamp'), table_name='web_development_post')
    op.drop_table('web_development_post')
    # ### end Alembic commands ###
