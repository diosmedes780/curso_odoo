# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MovieShowing(models.Model):
    _name = 'movie.showing'
    _description = 'Movie Showing'

    movie_id = fields.Many2one('cinema.movie', string='Movie')
    movie_theater_id = fields.Many2one('movie.theater', string='Movie theater')
    theater_room_id = fields.Many2one('theater.room', string='Theater room')
    seats_number = fields.Integer(related='theater_room_id.seats_number', store=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    total_attendees = fields.Integer(string='Total audience', compute='_compute_total_attendees', store=True)
    date_start = fields.Datetime(string='Date start')
    date_end = fields.Datetime(string='Date end')

    @api.depends('attendee_ids')
    def _compute_total_attendees(self):
        for showing in self:
            showing.total_attendees = len(showing.attendee_ids)
