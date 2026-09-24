# -*- coding: utf-8 -*-
{
    'name': 'OWL Training',
    'version': '19.0.1.0.0',
    'summary': 'Módulo de práctica para el curso de OWL',
    'category': 'Tools',
    'depends': ['web'],
    'data': [
        'views/actions.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'owl_training/static/src/basic/**/*',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}