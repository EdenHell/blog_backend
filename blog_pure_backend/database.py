import os
# noinspection PyProtectedMember
from flask import _app_ctx_stack
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData

database_url = os.environ['database_url']  # example: "postgresql+pg8000://user:password@host/blog"
engine = create_engine(database_url)
metadata = MetaData(engine)
session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory, scopefunc=_app_ctx_stack.__ident_func__)
