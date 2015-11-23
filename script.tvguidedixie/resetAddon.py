#
#      Copyright (C) 2014 Richard Dean
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmc
import xbmcaddon
import os

import sfile
import dixie

ottv     = xbmcaddon.Addon('script.on-tapp.tv')
ottvdir  = ottv.getAddonInfo('profile')
ottvskin = os.path.join(ottvdir, 'skins')
settings = xbmc.translatePath('special://profile/settings.bak')

OTTVURL  = ottv.getSetting('ottv.url').upper()
OTEPGURL = dixie.GetSetting('dixie.url').upper()

def resetAddon():
    if OTEPGURL == 'OTHER':
        ottv.setSetting('ottv.url', 'other')
        ottv.setSetting('SKIN',     'OTT-Skin')
    
    if OTTVURL == 'OTHER':
        dixie.SetSetting('dixie.url',  'Other')
        dixie.SetSetting('dixie.skin', 'EPG-Skin')
        
    try:
        sfile.rmtree(dixie.PROFILE)
        sfile.rmtree(ottvskin)
        sfile.remove(settings)
        ottv.setSetting('FIRSTRUN', 'false')
        dixie.SetSetting('logo.type', '0')
        dixie.SetSetting('dixie.logo.folder', 'None')
    except:
        pass
    dixie.DialogOK('On-Tapp.TV successfully reset.', 'It will be re-created next time', 'you start the guide')


if __name__ == '__main__':
    resetAddon()
