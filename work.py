# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Work']
__metaclass__ = PoolMeta


class Work:
    __name__ = 'project.work'

    @classmethod
    def __setup__(cls):
        super(Work, cls).__setup__()
        # Add to_decide, and bug to project_invoice_method
        items = [('to_decide', 'To Decide'), ('bug', 'Bug')]
        for item in items:
            if item not in cls.project_invoice_method.selection:
                cls.project_invoice_method.selection.append(item)

    @staticmethod
    def _get_invoiced_hours_to_decide(works):
        return {}

    @staticmethod
    def _get_invoiced_amount_to_decide(works):
        return {}

    def _get_lines_to_invoice_to_decide(self):
        return []

    @staticmethod
    def _get_hours_to_invoice_to_decide(works):
        return {}

    @classmethod
    def _get_invoiced_hours_bug(cls, works):
        return cls._get_invoiced_hours_timesheet(works)

    @classmethod
    def _get_invoiced_amount_bug(cls, works):
        return cls._get_invoiced_amount_timesheet(works)

    def _get_lines_to_invoice_bug(self):
        return self._get_lines_to_invoice_effort()

    @classmethod
    def _get_hours_to_invoice_bug(cls, works):
        return cls._get_hours_to_invoice_timesheet(works)

    @staticmethod
    def default_project_invoice_method():
        return 'to_decide'
