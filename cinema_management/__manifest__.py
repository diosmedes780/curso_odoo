# -*- coding: utf-8 -*-
{
    'name': "Cinema Management",
    'summary': "Manages the logistic and sales of a multiple movie theaters",
    'author': "Alex Esteves",
    'version': '19.0.0.1',
    "category": "Movies",
    "license": "AGPL-3",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/movie_theater_views.xml',
        'views/theater_room_views.xml',
        'views/movie_showing_views.xml',
        'views/cinema_movie_views.xml',
        'views/customer_views.xml',
    ],
    "installable": True,
    "auto_install": False,
}