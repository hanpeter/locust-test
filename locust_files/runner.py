# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from locust import HttpLocust, TaskSet, task


class Task(TaskSet):
    @task
    def get(self):
        url = os.environ.get('LOCUST_GET_URL', None)
        params = os.environ.get('LOCUST_GET_PARAMS', None)

        if url is not None:
            response = self.client.get(
                url=url,
                params=params,
            )
            print(response.status_code)

    @task
    def post(self):
        url = os.environ.get('LOCUST_POST_URL', None)
        json = os.environ.get('LOCUST_POST_JSON', None)

        if url is not None:
            response = self.client.post(
                url=url,
                json=json,
            )
            print(response.status_code)


class Locust(HttpLocust):
    task_set = Task
    min_wait = os.environ.get('LOCUST_MIN_WAIT', 1000)
    max_wait = os.environ.get('LOCUST_MAX_WAIT', 1000)
