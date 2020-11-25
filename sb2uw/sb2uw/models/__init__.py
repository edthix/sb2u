# -*- coding: utf-8 -*-

"""
This file holds database and package global stuffs
"""

from flask_sqlalchemy import SQLAlchemy, BaseQuery
from datetime import datetime

def add_record_user_and_time_stamps(record, user, new_record=False):
    """
    Set userstamps and timestamps for a record
    """
    if new_record:
        record.created_by = user.id
        record.created_at = datetime.now()

    record.updated_by = user.id
    record.updated_at = datetime.now()

class QueryWithSoftDelete(BaseQuery):
    '''
    Soft delete. We don't want to really delete a row, so we will mark the row in db as
    `deleted` by having a `deleted` Boolean field.

    Read more : https://github.com/miguelgrinberg/sqlalchemy-soft-delete
    '''

    _with_deleted = False

    def __new__(cls, *args, **kwargs):
        obj = super(QueryWithSoftDelete, cls).__new__(cls)
        obj._with_deleted = kwargs.pop('_with_deleted', False)
        if len(args) > 0:
            super(QueryWithSoftDelete, obj).__init__(*args, **kwargs)
            return obj.filter_by(
                deleted=False) if not obj._with_deleted else obj
        return obj

    def __init__(self, *args, **kwargs):
        pass

    def with_deleted(self):
        return self.__class__(db.class_mapper(self._mapper_zero().class_),
                              session=db.session(), _with_deleted=True)

    def _get(self, *args, **kwargs):
        # this calls the original query.get function from the base class
        return super(QueryWithSoftDelete, self).get(*args, **kwargs)

    def get(self, *args, **kwargs):
        # the query.get method does not like it if there is a filter clause
        # pre-loaded, so we need to implement it using a workaround
        obj = self.with_deleted()._get(*args, **kwargs)
        return obj if obj is None or self._with_deleted or not obj.deleted else None
