import logging
log_file_path = 'default_log.log'
logging.basicConfig(filename=log_file_path, level="DEBUG",
                    format='%(asctime)s-%(levelname)s-%(message)s')

Add = 356 * 9089
logging.debug(Add)
logging.info("This is Info")
logging.warning("this is warning")
logging.error("This is error")
logging.critical("This is critical")
try:
    a = 10/0
except Exception as e:
    logging.exception(e)
    print("except tell's to try-fun leave all error's in try-fun and expcept-fun shows the statement")
