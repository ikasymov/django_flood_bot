from sqlalchemy import *
from migrate import *

meta = MetaData()

girl = Table(
    'girl', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('url_path', Text(), nullable=False),
    Column('used', Boolean(), default=False, nullable=False)
)



def upgrade(migrate_engine):
    meta.bind = migrate_engine
    girl.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    girl.drop()
