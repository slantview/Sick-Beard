# Author: Steve Rude <steve@slantview.com>
# URL: http://code.google.com/p/sickbeard/
#
# This file is part of Sick Beard.
#
# Sick Beard is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Sick Beard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Sick Beard.  If not, see <http://www.gnu.org/licenses/>.

from tastekid.api import Similar

class :


class TasteKidRecommender(generic.Recommender):

    def __init__(self):

        generic.Recommender.__init__(self, "TasteKid")

        self.cache = TasteKidCache(self)

        self.url = 'http://www.tastekid.com/'

    def isEnabled(self):
        return sickbeard.TASTEKID


