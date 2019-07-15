# -*- coding: utf-8 -*-
{
   'name': "MT CBM Forex Exchange Rate",

    'summary': "Sync exchange rate from Central Bank of Myanmar",
    'description': """
        - Sync by Manual (Under Accounting > Configuration > CBM Forex)
        - If there has existing rate for the same date, it will override.
    """,
    'author': "MYAT THU",
    'version': '12.0.0.1.0',
    'depends': ['base','account',],
    'data': [
        "security/ir.model.access.csv",
        "views/views.xml",
        "data/mt_cbm_forex_setup.xml",
    ],
}
