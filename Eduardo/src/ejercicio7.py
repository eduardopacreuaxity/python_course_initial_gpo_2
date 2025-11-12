import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filename = "src/app.log"
)

logging.debug("Log nivel debug")
logging.info("Log nivel info")
logging.warning("Log nivel warning")
logging.error("Log nivel error")