#!/usr/bin/env python3
#
# Quick fixup script for the generated resources.
import json

WORKDIR='eosc-perf-client'

j = {}
with open(f'{WORKDIR}/package.json', 'r') as f:
    j = json.load(f)

if j['dependencies']['axios'] != '^0.26.1':
    j['dependencies']['axios'] = '^0.26.1'

if 'repository' not in j:
    j['repository'] = {
        'type': 'git',
        'url': 'git://github.com/eosc-perf-automation/eosc-perf-client.git'
    }

with open(f'{WORKDIR}/package.json', 'w') as f:
    json.dump(j, f, indent=2)