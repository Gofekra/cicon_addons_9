from openerp import models,fields,api
from calendar import Calendar
from datetime import datetime
from dateutil import rrule, parser
import sys

class MachinePreventiveStatusReport(models.AbstractModel): # Report File Name
    _name = 'report.cmms.report_machine_preventive_status_template'

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('cmms.report_machine_preventive_status_template')
        _docs = self._get_machine_list()
        docargs = {
            'doc_model': report.model,
            'docs': _docs,
            'get_intervals':self._get_intervals,
            'get_schedules':self._get_schedules
        }

        return report_obj.render('cmms.report_machine_preventive_status_template', docargs)

    def _get_machine_list(self):
        _qry = []
        if self._context.get('company_id'):
            _qry.append(('company_id', '=', self._context.get('company_id')))
        _machines = self.env['cmms.machine'].search(_qry)
        return _machines

    def _get_intervals(self,_machine_id):
        _tasks =  self.env['cmms.pm.task.master'].search([('pm_scheme_id', '=', _machine_id.pm_scheme_id.id)])
        _intervals = _tasks.mapped('interval_id')
        return _intervals

    def _get_schedules(self, _machine_id ,_interval_id ):
        _pm_schs = self.env['cmms.pm.schedule.master'].search([('pm_scheme_id', '=', _machine_id.pm_scheme_id.id),('interval_id', '=', _interval_id.id)])
        _pm_schs_machine = _pm_schs.filtered(lambda m:  _machine_id.id in  m.machine_ids._ids )
        if len(_pm_schs_machine) ==1:
            return _pm_schs_machine.next_date

MachinePreventiveStatusReport()