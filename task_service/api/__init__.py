#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Charles on 19-3-30
# Function: 
"""
Task Service对外提供的API,包括任务的启动、暂停、取消、更新等
"""

from .api import (start_task, clean_environment, update_results, pause_task, resume_task, cancel_task,
                  restart_all_tasks, start_all_new_tasks)