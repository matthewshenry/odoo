from odoo import models, fields
from odoo import api
class Raft(models.Model):
    _name = 'wrms.raft'
    _rec_name = 'boat_name'
    _description = 'Boat'


    guide_name = fields.Selection([('will', 'Will'), ('lauren', 'Lauren'), ('finn', 'Finn'), ('dani', 'Dani')], required=True, string="Guide")
    boat_name = fields.Char(string='Boat Name', required=True)
    capacity = fields.Integer(string='Boat Capacity', required=True)
    num_passengers = fields.Integer(compute='_compute_num_guests', string='# of Passengers', required=True)
    party_ids = fields.One2many(
        comodel_name='wrms.party', inverse_name='raft_id', string='Parties'
    )
    visitor_ids = fields.One2many(
        comodel_name='res.partner', inverse_name='raft_id', string='Visitors'
    )
    trip_id = fields.Many2one(
        comodel_name='wrms.trip', string='Trip'
    )
    @api.depends('party_ids')
    def _compute_num_guests(self):
        for raft in self:
            raft.num_passengers = 0
            for party in raft.party_ids:
                raft.num_passengers += party.num_passengers
