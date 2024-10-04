from odoo import models, fields, api
import logging
logger = logging.getLogger(__name__)

class Trip(models.Model):
    _name = 'wrms.trip'
    _description = 'Trip'
    _rec_name = 'section'

    am_pm = fields.Selection([('am', 'AM'), ('PM', 'PM')], required=True, string="AM/PM")
    section = fields.Selection([('numbers', 'Numbers'), ('Browns Canyon', 'Browns Canyon'), ('Pines Creek', 'Pines Creek')], string='Section', required=True)
    trip_date = fields.Date(string='Trip Date', required=True)
    num_passengers = fields.Integer(compute='_compute_num_guests', string='# of Passengers')
    booking_ids = fields.One2many(
        comodel_name ='wrms.booking', inverse_name='trip_id', string='Bookings'
    )
    party_ids = fields.Many2many(
        comodel_name='wrms.party', compute='_compute_trip_party', string='Parties'
    )
    raft_ids = fields.One2many(
        comodel_name='wrms.raft', inverse_name='trip_id', string='Rafts'
    )
    visitor_ids = fields.One2many(
        comodel_name='res.partner', compute='_compute_trip_visitors', string='Visitors'
    )
    is_created = fields.Boolean(default=False, string="Is Created")


    @api.depends('party_ids')
    def _compute_num_guests(self):
        for trip in self:
            trip.num_passengers = 0
            for party in trip.party_ids:
                trip.num_passengers += party.num_passengers

    def _compute_display_name(self):
        for trip in self:
            trip.display_name = f"{trip.trip_date} {trip.section} {trip.am_pm}"

    @api.depends('booking_ids')
    def _compute_trip_party(self):
        for trip in self:
            logger.info("\n _compute_trip_party is being called for %s" % trip.display_name)
            if trip.booking_ids:
                trip.party_ids = trip.booking_ids.party_id
            else:
                trip.party_ids = []

    @api.depends('booking_ids')
    def _compute_trip_visitors(self):
        for trip in self:
            if trip.booking_ids:
                trip.visitor_ids = trip.booking_ids.visitor_ids
            else:
                trip.visitor_ids = []