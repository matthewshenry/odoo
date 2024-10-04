{
    'name': 'Whitewater Rafting Management System',
    'version': '17.0.0.0',
    'category': 'Services',
    'summary': 'Rafting Trip Booking System for Outfitters',
    'description': 'A system wherein raft guide outfitters can manage their reservations and outfit trips.',
    'depends': ['base', 'mail'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/party_view.xml',
        'views/raft_view.xml',
        'views/visitor_view.xml',
        'data/party_data.xml',
        'views/trip_view.xml',
        'views/booking_view.xml',
        'data/visitor_data.xml',
        'data/ir_cron_data.xml',
        'views/wizard_views/cancel_booking_wizard_view.xml',
        'views/wizard_views/reset_booking_wizard_view.xml',
        'views/wizard_views/booking_trip_wizard_view.xml',
        'report/report_trip_template.xml',
        'report/action_report_trip.xml',
        'report/report_header.xml'

    ],
    'installable': True,
    'application': True,
}

