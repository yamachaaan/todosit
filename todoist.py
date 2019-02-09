#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from pytodoist import todoist
from lib.date import Date

date = Date()
class Todoist():
    def login(self,API_TOKEN):
        user = todoist.login_with_api_token(API_TOKEN)
        return user

    def get_projects(self, user):
        return  user.get_projects()

    def get_tasks(self, user, query=None):
        if query is None:
            tasks = user.get_tasks()
            print('ALL TASK:')
            print('----------------------------------------')
        else:
            print('OVER DUE & TODAY\'s TASK:')
            print('----------------------------------------')
            now = date.get_now()
            tasks =  user.search_tasks(todoist.Query.OVERDUE, todoist.Query.TODAY)
        for task in tasks:
            if not task.due_date_utc is None:
                due_date_jst = date.date_to_str(date.utc_to_jst(date.str_to_date(task.due_date_utc)))
            else:
                due_date_jst = ''
            print(str(task.id) + ' ' + task.project.name + ' ' + task.content + ' ' + due_date_jst)

    def add_task(self, content, projects, project=None, due=None):
        print(content)
        return

    def complete_task(self, user, content):
        tasks = user.get_tasks()
        for task in tasks:
            if task.id == int(content):
                print('project_name: ' + task.project.name + ' task_name: ' + task.content)
                proceed = input('Proceed (y/n)?')
                if proceed is 'y':
                    task.complete()
                elif proceed is 'n':
                    print('canceled')
        return
