import logging
import traceback
import typer

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def recreate_base():
    try:
        logger.info("Recreating base...")
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    typer.run(recreate_base())