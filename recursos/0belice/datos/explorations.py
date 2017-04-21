# -*- coding: utf-8 -*-

from gettext import gettext as _

EXP1 = [
    _('Districts'),
    ['lineasDepto'],
    [],
    ['deptos']
]

EXP2 = [
    _('District capitals'),
    ['lineasDepto', 'capitales'],
    [],
    ['capitales']
]

EXP3 = [
    _('Cities'),
    ['lineasDepto', 'capitales', 'ciudades'],
    [],
    ['capitales', 'ciudades']
]

EXP4 = [
    _('Waterways'),
    ['rios'],
    [],
    ['rios']
]

EXP5 = [
    _('Routes'),
    ['rutas', 'capitales'],
    ['capitales'],
    ['rutas']
]

EXPLORATIONS = [EXP1, EXP2, EXP3, EXP4, EXP5]

