###

import supybot.conf as conf
import supybot.registry as registry

try:
    from supybot.i18n import PluginInternationalization

    _ = PluginInternationalization("VCPR")
except:
    _ = lambda x: x


def configure(advanced):
    from supybot.questions import expect, anything, something, yn

    conf.registerPlugin("VCPR", True)
    if advanced:
        output("The VCPR Plugin displays a random quote from GTA5's Vice City Public Radio")


Vcpr = conf.registerPlugin("VCPR")

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
