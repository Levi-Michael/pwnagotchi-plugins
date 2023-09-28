import discord, logging, subprocess
from os import remove
from pwnagotchi.utils import StatusFile
import pwnagotchi.ui.components as components
import pwnagotchi.ui.view as view
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins

class discoBoss(plugins.Plugin):
    __author__ = 'A1buS'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = '''
    discoBoss Discord bot for pwnagotchi manage
    '''
    def __init__(self):
        self.ready = False
        self.TOKEN = '<TOKEN>'
        self.DEFAULT_MESSAGES_LIMIT = 100

        self.discoBoss_channel = dict({
                                'name': 'discoboss',
                                'channel_id': '<CHANNEL_ID>',
                                'webhook_name':'discoBoss_WH'
                                })

        self.discoHash_channel = dict({
                                'name': 'disco-hashes',
                                'channel_id': '<CHANNEL_ID>',
                                'webhook_name':'discohash_WH'
                                })
        logging.info("[discoBoss]: discoBoss plugin initialize")

