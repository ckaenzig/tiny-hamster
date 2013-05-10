#!/usr/bin/env python

import os
from xmlrpclib import ServerProxy, Error

class TinyXMLRPC:
  def __init__(self, username, password, database, base_url):
    self.username = username
    self.password = password
    self.database = database
    self.base_url = base_url

    self._connect()
    self._login()

  def _connect(self):
    self._common_server = ServerProxy(os.path.join(self.base_url, "common"))
    self._object_server = ServerProxy(os.path.join(self.base_url, "object"))
    self._wizard_server = ServerProxy(os.path.join(self.base_url, "wizard"))

  def _login(self):
    self.user_id = self._common_server.login(self.database, self.username, self.password)

  def execute(self, *params):
    return self._object_server.execute(self.database, self.user_id, self.password, *params)

  def wizard(self, *params):
    return self._wizard_server.execute(self.database, self.user_id, self.password, *params)


class TinyServer (TinyXMLRPC):

  # return a list of analytical accounts matching the search
  #  each account is a list [ account_id, account_name ]
  def search_account(self, search):
    return self.execute("account.analytic.account", "name_search", search)

  def search_task(self, account_id, search):
    return self.execute("project.task", "name_search", search, [["state", "=", "open"]], "ilike", {"lang": "fr_FR", "name_search": search, "account_id": account_id})

  def search_timesheet(self, date):
    return self.execute("hr_timesheet_sheet.sheet", "search", [["user_id", "=", self.user_id], ["state", "=", "draft"], ["date_from", "<=", date]], 0.0, 80.0, 0, {"lang": "fr_FR", "active_ids": [], "active_id": 480})

  def timesheet_defaults(self):
    return self.execute("hr.analytic.timesheet", "default_get", ["user_id", "account_id", "general_account_id", "product_uom_id", "journal_id", "name", "to_invoice", "amount", "unit_amount", "activity", "date", "product_id"], {"lang": "fr_FR", "user_id": self.user_id})

  def attendance_defaults(self):
    return self.execute("hr.attendance", "default_get", ["action", "employee_id"], {"lang": "fr_FR", "user_id": self.user_id}) 

  def current_timesheet_wiz(self):
    return self.wizard(208, {"form": {}, "ids": [], "report_type": "pdf", "model": "ir.ui.menu", "id": 481}, "init", {"lang": "fr_FR"})

  def invoice_factor(self, something):
    return self.execute("hr_timesheet_invoice.factor", "name_get", [something], {"lang": "fr_FR"})

  def on_change_unit_amount(self, product_id, amount, product_uom_id):
    return self.execute("hr.analytic.timesheet", "on_change_unit_amount", [], product_id, amount, product_uom_id)

  def on_change_account_id(self, account_id):
    return self.execute("hr.analytic.timesheet", "on_change_account_id", [], account_id)

  def timesheet_create(self, ts_lines, att_lines):
    return self.execute("hr_timesheet_sheet.sheet", "create", {"timesheet_ids": ts_lines, "user_id": self.user_id, "name": "2011 Semaine 4", "date_from": date_from, "attendances_ids": att_lines, "date_current": date_current, "date_to": date_to}, {"lang": "fr_FR", "active_ids": active_ids, "active_id": active_id})

  def timesheet_write(self, ts_id, ts_lines, att_lines=[]):
    return self.execute("hr_timesheet_sheet.sheet", "write", [ts_id], {"timesheet_ids": ts_lines, "attendances_ids": att_lines}, {"lang": "fr_FR", "active_ids": [], "read_delta": 0.0, "active_id": 0})
