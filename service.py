import xbmc, xbmcgui, subprocess, os, sys, urllib, re
import xbmcplugin, xbmcaddon


__scriptID__      = "plugin.makemkvbluray"
__addon__ = xbmcaddon.Addon(__scriptID__)

# Shared resources
BASE_RESOURCE_PATH = os.path.join( __addon__.getAddonInfo('path'), "resources" )
sys.path.append( os.path.join( BASE_RESOURCE_PATH, "lib" ) )

import makemkv

__language__ = __addon__.getLocalizedString
_ = sys.modules[ "__main__" ].__language__

import settings, file, mkvparser, brlog, makemkv

_log = brlog.BrLog('tracker service')

_log.info('Starting the BluRay tracker service') #@UndefinedVariable

class MyPlayer(xbmc.Player):
    def __init__(self):
        xbmc.Player.__init__(self)
        self.makemkv = makemkv.MakeMkvInteraction()
    
    def onPlayBackStopped(self):
        _log.info('Playback stopped, trying to kill makemkv')
        xbmc.executebuiltin('Notification("MakeMkv", "Playback ended, stopping makemkv")')
        self.makemkv.killMkv()

    def onPlayBackStarted(self):
        _log.info('Playback started')
        


myPlayer = MyPlayer()

while (not xbmc.abortRequested):
    xbmc.sleep(4)