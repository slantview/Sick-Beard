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

__all__ = ['tastekid', 'jinni']

import sickbeard

from os import sys

def sortedRecommenderList():

    initialList = sickbeard.recommenderList
    recommenderDict = dict(zip([x.getID() for x in initialList], initialList))

    newList = []

    # add all modules in the priority list, in order
    for curModule in sickbeard.RECOMMENDER_ORDER:
        if curModule in recommenderDict:
            newList.append(recommenderDict[curModule])

    # add any modules that are missing from that list
    for curModule in recommenderDict:
        if recommenderDict[curModule] not in newList:
            newList.append(recommenderDict[curModule])

    return newList

def makeRecommenderList():

    return [x.recommender for x in [getRecommenderModule(y) for y in __all__] if x]


def getRecommenderModule(name):
    name = name.lower()
    prefix = "sickbeard.recommenders."
    if name in __all__ and prefix+name in sys.modules:
        return sys.modules[prefix+name]
    else:
        raise Exception("Can't find "+prefix+name+" in "+repr(sys.modules))

def getRecommenderClass(id):

    recommenderMatch = [x for x in sickbeard.recommenderList if x.getID() == id]

    if len(recommenderMatch) != 1:
        return None
    else:
        return recommenderMatch[0]

class RecommenderSearcher():
    def run(self):
        try:
            show_list = sickbeard.showList
            for r in sickbeard.recommenderList:
                results = r.search(show_list)
                for cur_name in results
                     try:
                        t = tvdb_api.Tvdb(custom_ui=classes.ShowListUI, **sickbeard.TVDB_API_PARMS)

                        self._log(u"Looking up name "+cur_name+u" on TVDB", logger.DEBUG)
                        showObj = t[cur_name]
                    except (tvdb_exceptions.tvdb_exception):
                        # if none found, search on all languages
                        try:
                            # There's gotta be a better way of doing this but we don't wanna
                            # change the language value elsewhere
                            ltvdb_api_parms = sickbeard.TVDB_API_PARMS.copy()

                            ltvdb_api_parms['search_all_languages'] = True
                            t = tvdb_api.Tvdb(custom_ui=classes.ShowListUI, **ltvdb_api_parms)

                            self._log(u"Looking up name "+cur_name+u" in all languages on TVDB", logger.DEBUG)
                            showObj = t[cur_name]
                        except (tvdb_exceptions.tvdb_exception, IOError):
                            pass

                        continue
                    except (IOError):
                        continue

                    show_exists = sickbeard.helpers.findCertainShow(sickbeard.showList, int(show.tvdbid))

                    if show_exists:
                        logger.log("An existing tvdbid already exists in the database. Skipping.")
                        continue

                    tvdbName = None
                    tvdbResult = CMD_SickBeardSearchTVDB([], {"tvdbid": showObj.tvdbid}).run()

                    if tvdbResult['result'] == result_type_map[RESULT_SUCCESS]:
                        if len(tvdbResult['data']['results']) == 1 and 'name' in tvdbResult['data']['results'][0]:
                            tvdbName = tvdbResult['data']['results'][0]['name']

                    if not tvdbName:
                        logger.log("Unable to retrieve information from tvdb")

                    sickbeard.showQueueScheduler.action.addShow(int(showObj.tvdbid), self.location, sickbeard.STATUS_DEFAULT, newQuality, int(self.season_folder)) #@UndefinedVariable

        except:
            self.amActive = False
            raise
