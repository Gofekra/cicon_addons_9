{
    'name': 'CICON HR Equipment Extended',
    'version': '0.1',
    'author': 'CICON',
    'sequence': 99,
    'summary': 'CICON HR Equipment',
    'description': """CICON HR Equipment""",
    'website': 'http://www.cicon.net',
    'category': 'CICON IT',
    'depends': ['hr_equipment'],
    'data': [
        'security/cicon_hr_equipment_security.xml',
        'security/ir.model.access.csv',
        'cicon_hr_equipment_view.xml',
        'cicon_hr_equipment_property_view.xml',
    ],
    'update_xml': [],
    'description': 'CICON Applications',
    'active': False,
    'installable': True,
    'application': False,
    'auto_install': False
}
