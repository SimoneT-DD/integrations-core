# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.dev import get_docker_hostname, get_here, load_jmx_config

HERE = get_here()
HOST = get_docker_hostname()
PORT = 9000
PROJECT = 'org.sonarqube:sonarqube-scanner'
JMX_WEB_INSTANCE = {'host': HOST, 'port': 10443, 'is_jmx': True}
JMX_CE_INSTANCE = {'host': HOST, 'port': 10444, 'is_jmx': True}
WEB_INSTANCE = {
    'web_endpoint': 'http://{}:{}'.format(HOST, PORT),
    'components': {PROJECT: {'tag': 'project'}},
    'tags': ['foo:bar'],
}

COMPOSE_FILE = os.getenv('COMPOSE_FILE')

CHECK_CONFIG = load_jmx_config()
CHECK_CONFIG['instances'] = [JMX_WEB_INSTANCE, JMX_CE_INSTANCE, WEB_INSTANCE]