# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

import requests
import time

class MTCbmForexHistory(models.TransientModel):
    _name = "mt.cbm.forex.history"
    _description = "CBM Forex History"

    name = fields.Datetime(string = 'Sync Date', default = fields.datetime.now())
    data = fields.Text(string = 'Sync Data')

    @api.multi
    def get_latest_rate(self):
        api_url = self.env["ir.config_parameter"].sudo().get_param("mt_cbm_forex_url")
        response = requests.get(api_url).json()
        rates = response.get('rates')
        updated_date = time.strftime('%Y-%m-%d', time.localtime(int(response.get('timestamp'))))
        active_currencies = self.env['res.currency'].search([])
        list_active_currencies_name = active_currencies.mapped('name')

        for currency,rate in rates.items():
            if currency in list_active_currencies_name:
                if self.env.user.company_id.currency_id.name not in list(rates.keys()):
                    rate =  1/float(rate.replace(',',''))
                else:
                    rate = float(rate.replace(',',''))
                currency_id = active_currencies.search([('name','=',currency)]).id
                existing_rate = self.env['res.currency.rate'].search([('name','=',updated_date),('currency_id','=',currency_id)])
                if not existing_rate:
                    vals={}
                    vals.update({
                                'name': updated_date,
                                'rate':  rate,
                                'currency_id': currency_id
                               })
                    self.env['res.currency.rate'].create(vals)

                else:
                    existing_rate.write({'rate': rate})

        return self.create({'name': time.strftime('%Y-%m-%d %H:%M%S', time.localtime(int(response.get('timestamp')))),'data': response})


