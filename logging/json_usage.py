import json
import logging
import logging.config

with open("setting.json", "rt") as file:
  config = json.load(file)
  
logging.config.dictConfig(config)
logger = logging.getLogger()

logger.info("Test Message")