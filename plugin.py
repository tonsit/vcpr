###
from supybot.commands import *
import supybot.conf as conf
import supybot.log as log
import supybot.utils as utils
import supybot.plugins as plugins
import supybot.callbacks as callbacks
import random

try:
    from supybot.i18n import PluginInternationalization

    _ = PluginInternationalization("VCPR")
except ImportError:
    _ = lambda x: x


class VCPR(callbacks.Plugin):
    """GTA Vice City Public Radio"""

    threaded = True
    public = True
    botNick = False

    def __init__(self, irc):
        self.__parent = super(VCPR, self)
        self.__parent.__init__(irc)
        self.quotefile = '/home/scott/gambot/plugins/VCPR/vcpr.txt'
 
    def getQuote(self, text):
        if text:
            return self.searchLine(text)
        return self.randomLine()
    
    def searchLine(self, search):
        with open(self.quotefile) as f:
            lines = f.read().splitlines()
            for line in lines:
                if (search in line): 
                    return line
        return f"No match found to '{search}'"

    def randomLine(self):
        with open(self.quotefile) as f:
            lines = f.read().splitlines()
            return random.choice(lines)

    def vcpr(self, irc, msg, args, text):
        """Getting random quote"""
        channel = msg.args[0]
        if not irc.isChannel(channel):
            channel = msg.nick
        response = self.getQuote(text)
        if response:
            irc.reply(response)

    vcpr = wrap(vcpr, [optional("text")])

Class = VCPR

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
