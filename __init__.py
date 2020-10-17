###

"""
VCPR: Enables the bot to respond to !VCPR with a random quote from Vice City Public Radio from GTA5.
"""

import supybot
import supybot.world as world

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = "2020.10.17"

# XXX Replace this with an appropriate author or supybot.Author instance.
__author__ = supybot.Author("tonsit", "tonsit", "supybot@tonsit.com")

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

# This is a url where the most recent plugin package can be downloaded.
__url__ = "https://github.com/tonsit/vcpr/"

from . import config
from . import plugin
from imp import reload

reload(config)
reload(plugin)

if world.testing:
    from . import test

Class = plugin.Class
configure = config.configure

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
