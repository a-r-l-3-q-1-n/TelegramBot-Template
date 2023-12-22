from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from Database.Models import *
from Utils.Logger import Logger
from Settings.Config import DATABASE


class Database:

    def __init__(self):

        # Session
        self.engine = create_async_engine(url=DATABASE, echo=True)
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False)

        # Logger
        self.logger = Logger()

    # --> INIT METHODS

    async def init_all(self):
        try:
            async with self.engine.begin() as connection:
                await connection.run_sync(Base.metadata.create_all)

                # <code> ...

            self.logger.log_info(f"[INFO] -> Created/Initialized database")
        except SQLAlchemyError as exception:
            self.logger.log_error(f"[FAIL] -> while connecting to database: {exception}")
