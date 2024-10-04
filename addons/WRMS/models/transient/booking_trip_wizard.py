from odoo import models, fields, api

class BookingTripWizard(models.TransientModel):
    _name = 'booking.trip.wizard'
    _description = 'Booking Trip Wizard'
    am_pm = fields.Selection([('am', 'AM'), ('PM', 'PM')], required=True, string="AM/PM")
    section = fields.Selection([('numbers', 'Numbers'), ('Browns Canyon', 'Browns Canyon'), ('Pines Creek', 'Pines Creek')], string='Section',required=True)
    trip_date = fields.Date(string='Trip Date', required=True)
    booking_id = fields.Many2one('wrms.booking', string='Booking')

    def action_select_trip(self):
        # Gets the booking with the new booking_id so that we can update its trip to the one we're making/selecting
        booking_id = self.env.context.get('active_id')
        booking = self.env['wrms.booking'].browse(booking_id)

        trip = self.env['wrms.trip'].search([
            ('trip_date', '=', self.trip_date),
            ('am_pm', '=', self.am_pm),
            ('section', '=', self.section)
        ], limit=1)
        if not trip:
            trip = self.env['wrms.trip'].create({
                'trip_date': self.trip_date,
                'am_pm': self.am_pm,
                'section': self.section,
            })
        booking.write({'trip_id': trip.id})
        return {'type': 'ir.actions.act_window_close'}
