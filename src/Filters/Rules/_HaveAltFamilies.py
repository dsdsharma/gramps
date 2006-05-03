#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2002-2006  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id$

#-------------------------------------------------------------------------
#
# Standard Python modules
#
#-------------------------------------------------------------------------
from gettext import gettext as _

#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
from _Rule import Rule
from RelLib import ChildRefType

#-------------------------------------------------------------------------
# "People who were adopted"
#-------------------------------------------------------------------------
class HaveAltFamilies(Rule):
    """People who were adopted"""

    name        = _('Adopted people')
    description = _("Matches people who were adopted")
    category    = _('Family filters')

    def apply(self,db,person):
        for (fam,rel1,rel2) in person.get_parent_family_handle_list():
            if rel1 == ChildRefType.CHILD_ADOPTED \
                   or rel2 == ChildRefType.CHILD_ADOPTED:
                return True
        return False
