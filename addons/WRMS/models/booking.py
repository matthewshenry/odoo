from odoo import models, fields, api
from datetime import date
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class Booking(models.Model):
    _name = 'wrms.booking'
    _description = 'Booking'
    _inherit = ['mail.thread']

    name = fields.Char(string='Booking Reference')
    stage = fields.Selection([('pending', 'Pending'), ('checked-in', 'Checked-In'), ('complete', 'Complete'), ('canceled', 'Canceled')], string='Stage', default='pending', help="Status of the booking: bookings are 'checked-in' when the party has been assigned a raft for the trip, 'complete' when the trip is completed, and 'canceled' if the booking becomes canceled.")
    trip_id = fields.Many2one(
        comodel_name='wrms.trip', string='Trip'
    )
    party_id = fields.Many2one(
        comodel_name='wrms.party', string='Party'
    )
    visitor_ids = fields.One2many(
        comodel_name='res.parnter', compute='_compute_booking_visitors', string='Guests'
    )
    cancellation_reason = fields.Text(string='Cancellation Reason')

    am_pm = fields.Selection(related='trip_id.am_pm', string="AM/PM")
    section = fields.Selection(related='trip_id.section', string='Section')
    trip_date = fields.Date(related='trip_id.trip_date', string='Trip Date')
    head_of_party = fields.Char(related='party_id.head_of_party', string='Head of Party')

    show_check_in_button = fields.Boolean(compute='_compute_show_check_in_button')
    show_complete_button = fields.Boolean(compute='_compute_show_complete_button')
    show_cancel_button = fields.Boolean(compute='_compute_show_cancel_button')
    show_reset_button = fields.Boolean(compute='_compute_show_reset_button')

    # def write(self, vals):
    #     result = super(Booking, self).write(vals)
    #     # Check if the stage needs to be updated to 'checked-in'
    #     for record in self:
    #         if record.stage == 'pending' and record.party_id.raft_id:
    #             record.stage = 'checked-in'
    #     return result

    @api.model
    def update_booking_status(self):
        today = date.today()
        bookings_to_complete = self.search([
            ('stage', '=', 'checked-in'),
            ('trip_date', '<', today)
        ])
        for booking in bookings_to_complete:
            booking.write({'stage': 'complete'})

    @api.onchange('trip_id', 'party_id')
    def _onchange_trip_party(self):
        if self.trip_id and self.party_id:
            self.visitor_ids = self.party_id.visitor_ids.ids

    @api.depends('party_id')
    def _compute_booking_visitors(self):
        for booking in self:
            if booking.party_id:
                booking.visitor_ids = booking.party_id.visitor_ids.ids
            else:
                booking.visitor_ids = []

    def action_set_checked_in(self):
        self.stage = 'checked-in'

    def action_set_completed(self):
        self.stage = 'complete'

    def action_set_canceled(self):
        self.stage = 'canceled'

    def action_set_pending(self):
        self.stage = 'pending'

    def action_open_booking_trip_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Select Trip',
            'res_model': 'booking.trip.wizard',
            'view_mode': 'form',
            'target': 'new',
        }

    def action_open_cancel_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cancel Booking',
            'res_model': 'cancel.booking.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_booking_id': self.id},
        }

    def action_open_reset_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reset Booking',
            'res_model': 'reset.booking.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_booking_id': self.id},
        }