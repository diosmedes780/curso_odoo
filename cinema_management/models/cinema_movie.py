# -*- coding: utf-8 -*-

from odoo import models, fields


class CinemaMovie(models.Model):
    _name = 'cinema.movie'
    _description = 'Movie'

    name = fields.Char(string='Name')
    category = fields.Selection([('sci_fi', 'Sci-fi'), ('thriller', 'thriller'),
                                 ('action', 'Action'), ('comedy', 'Comedy')], string='Category')
    rating = fields.Selection([('g_rating', 'G'), ('pg_rating', 'PG'), ('pg12_rating', 'PG-13'),
                               ('r_rating', 'R'), ('nc17_rating', 'NC-17')], string='Rating')
    showing_ids = fields.One2many('movie.showing', 'movie_id', string='Showings')
    review_ids = fields.One2many('movie.review', 'movie_id', string='Reviews')
