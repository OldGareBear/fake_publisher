#!/usr/bin/env python
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "partnerblog.settings")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "partnerblog.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
