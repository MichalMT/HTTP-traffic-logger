#!/usr/bin/env python

import ifcfg
import inquirer

def select_interface():
    interfaces = []
    for name, interface in ifcfg.interfaces().items():
        interfaces.append(name)

    questions = [
      inquirer.List('interface',
                    message="Select interface >>",
                    choices=interfaces,
                ),
    ]
    answers = inquirer.prompt(questions)

    interface = answers["interface"]

    return interface
