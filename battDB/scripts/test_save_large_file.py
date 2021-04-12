#!/usr/bin/env python3

from battDB.models import ExperimentDataFile


def run():
    exp18 = ExperimentDataFile.objects.get(id=18)
    exp18.clean()
    exp18.save()
