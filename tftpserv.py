from tftpy import TftpServer
import logging

logging.basicConfig(level=logging.DEBUG)
server = TftpServer('.')  # Change this!
server.listen('0.0.0.0', 69)