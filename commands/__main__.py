import logging
import traceback
import typer

from commands.seed_bass_guitars import seed_bass_guitars
from dependencies.database import database_engine
from dependencies.models.base_model import DeclarativeBase

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def recreate_base():
    try:
        logger.info("Recreating base...")
        DeclarativeBase.metadata.drop_all(database_engine)
        DeclarativeBase.metadata.create_all(database_engine)
        seed_bass_guitars()
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    typer.run(recreate_base)