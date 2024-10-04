from odoo import models, fields, api

class ResetBookingWizard(models.TransientModel):
    _name = 'reset.booking.wizard'
    _description = 'Booking Reset Confirmation'

    booking_id = fields.Many2one('wrms.booking', string='Booking', required=True)

    def action_confirm_reset(self):
        self.booking_id.action_set_pending()
        return {'type': 'ir.actions.act_window_close'}

    def action_reset(self):
        return {'type': 'ir.actions.act_window_close'}
