# -*- coding: utf-8 -*-
# © 2008-2014 Alistek
# © 2016 Savoir-faire Linux
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl).

{
    'name': 'Aeroo Reports',
    'version': '2.0.0',
    'category': 'Generic Modules/Aeroo Reports',
    'summary': 'Enterprise grade reporting solution',
    'author': 'Alistek',
    'website': 'http://www.alistek.com',
    'complexity': "easy",
    'depends': ['mail'],
    'external_dependencies': {
        'python': ['aeroolib', 'genshi', 'simplejson'],
    },
    'data': [
        "security/security.xml",
        "views/ir_actions_report.xml",
        "views/mail_template.xml",
        "data/ir_config_parameter.xml",
        "data/report_aeroo_data.xml",
        "security/ir.model.access.csv",
    ],
    'demo': ["demo/report_sample.xml"],
    "license": "GPL-3 or any later version",
    'installable': True,
    'application': True,
}
