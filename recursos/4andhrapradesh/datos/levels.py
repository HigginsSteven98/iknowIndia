# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        1,
        _('Divisions'),
        ['lineasDepto'],
        [],
[
    (_('Adilabad'), 1, _('Adilabad'), _("It's in the north")),
    (_('Nizamabad'), 1, _('Nizamabad'), _("It's in the northwest")),
    (_('Karimnagar'), 1, _('Karimnagar'), _("It's in the north")),
    (_('Medak'), 1, _('Medak'), _("It's in the northwest")),
    (_('Warangal'), 1, _('Warangal'), _("It's in the north")),
    (_('Rangareddy'), 1, _('Rangareddy'), _("It's in the west")),
    (_('Nalgonda'), 1, _('Nalgonda'), _("It's in the center")),
    (_('Khammam'), 1, _('Khammam'), _("It's in the northeast")),
    (_('Mahabubnagar'), 1, _('Mahabubnagar'), _("It's in the west")),
    (_('Kamulu'), 1, _('Kamulu'), _("It's in the southwest")),
    (_('Ananthapur'), 1, _('Ananthapur'), _("It's in the southwest")),
    (_('Kadapa'), 1, _('Kadapa'), _("It's in the south")),
    (_('Chittoor'), 1, _('Chittoor'), _("It's in the south")),
    (_('Nelluru'), 1, _('Nelluru'), _("It's in the south")),
    (_('Prakasam'), 1, _('Prakasam'), _("It's in the south")),
    (_('Guntur'), 1, _('Guntur'), _("It's in the southeast")),
    (_('Krishna'), 1, _('Krishna'), _("It's in the east")),
    (_('West Godavari'), 1, _('West Godavari'), _("It's in the east")),
    (_('East Godavari'), 1, _('East Godavari'), _("It's in the east")),
    (_('Vishakhapatnam'), 1, _('Vishakhapatnam'), _("It's in the northeast")),
    (_('Vijayanagaram'), 1, _('Vijayanagaram'), _("It's in the northeast")),
    (_('Srikakulam'), 1, _('Srikakulam'), _("It's in the northeast"))
]
]

LEVEL2 = [
        2,
        _('Taluka Headquarters'),
        ['lineasDepto', 'capitales'],
        [],
[
    #(_('Panaji'), _("It's in %s taluka") % _('Tiswadi') + '\n' + _("It's in the west")),

]
]


LEVEL3 = [
        2,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    #(_('New Delhi'), _('It is in %s') % _('New Delhi')),
  
]
]

LEVELS = [LEVEL1]


