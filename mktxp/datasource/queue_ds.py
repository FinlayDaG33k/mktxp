# coding=utf8
## Copyright (c) 2020 Arseniy Kuznetsov
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.


from mktxp.datasource.base_ds import BaseDSProcessor


class QueueTreeMetricsDataSource:
    ''' Queue Tree Metrics data provider
    '''             
    @staticmethod    
    def metric_records(router_entry, *, metric_labels = None):
        if metric_labels is None:
            metric_labels = []                
        try:
            queue_tree_records = router_entry.api_connection.router_api().get_resource('/queue/tree/').get()
            return BaseDSProcessor.trimmed_records(router_entry, router_records = queue_tree_records, metric_labels = metric_labels)
        except Exception as exc:
            print(f'Error getting system resource info from router{router_entry.router_name}@{router_entry.config_entry.hostname}: {exc}')
            return None


class SimpleQueueMetricsDataSource:
    ''' Simple Queue Metrics data provider
    '''             
    @staticmethod    
    def metric_records(router_entry, *, metric_labels = None):
        if metric_labels is None:
            metric_labels = []                
        try:
            simple_queue_records = router_entry.api_connection.router_api().get_resource('/queue/simple/').get()
            return BaseDSProcessor.trimmed_records(router_entry, router_records = simple_queue_records, metric_labels = metric_labels)
        except Exception as exc:
            print(f'Error getting system resource info from router{router_entry.router_name}@{router_entry.config_entry.hostname}: {exc}')
            return None
