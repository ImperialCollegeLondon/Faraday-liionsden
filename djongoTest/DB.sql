[{"model": "battDB.testprotocol", "pk": 1, "fields": {"name": "PyBaMM example protocol", "attributes": {}, "description": "pybamm.Experiment(\r\n    [\r\n        \"Discharge at C/10 for 10 hours or until 3.3 V\",\r\n        \"Rest for 1 hour\",\r\n        \"Charge at 1 A until 4.1 V\",\r\n        \"Hold at 4.1 V until 50 mA\",\r\n        \"Rest for 1 hour\",\r\n    ]\r\n    * 3,", "parameters": {}}}, {"model": "battDB.manufacturer", "pk": 1, "fields": {"name": "BorkCorp", "attributes": {}}}, {"model": "battDB.manufacturer", "pk": 2, "fields": {"name": "Maccor", "attributes": {}}}, {"model": "battDB.equipmenttype", "pk": 2, "fields": {"name": "GalvoTron 3000", "attributes": {"channels": 10}, "manufacturer": 1}}, {"model": "battDB.equipment", "pk": 1, "fields": {"name": "Tom's GalvoTron 3000", "attributes": {}, "type": 2, "serialNo": "1234"}}, {"model": "battDB.cellseparator", "pk": 1, "fields": {"name": "MyMembrane", "attributes": {"material": null, "porosity_pct": null}}}, {"model": "battDB.cellbatch", "pk": 1, "fields": {"name": "foo", "attributes": {}, "manufactured_on": "2020-08-04", "manufacturer": 1, "cells_schema": {}}}, {"model": "battDB.cellconfig", "pk": 1, "fields": {"name": "4s", "attributes": {}}}, {"model": "battDB.cell", "pk": 1, "fields": {"name": "MyLiPo", "attributes": {}, "batch": 1}}, {"model": "battDB.experimentalapparatus", "pk": 1, "fields": {"name": "Tom's Lab", "attributes": {}, "cellConfig": null, "protocol": 1, "photo": "", "testEquipment": [1]}}, {"model": "contenttypes.contenttype", "pk": 1, "fields": {"app_label": "battDB", "model": "cell"}}, {"model": "contenttypes.contenttype", "pk": 2, "fields": {"app_label": "battDB", "model": "cellseparator"}}, {"model": "contenttypes.contenttype", "pk": 3, "fields": {"app_label": "battDB", "model": "equipment"}}, {"model": "contenttypes.contenttype", "pk": 4, "fields": {"app_label": "battDB", "model": "manufacturer"}}, {"model": "contenttypes.contenttype", "pk": 5, "fields": {"app_label": "battDB", "model": "signaltype"}}, {"model": "contenttypes.contenttype", "pk": 6, "fields": {"app_label": "battDB", "model": "testprotocol"}}, {"model": "contenttypes.contenttype", "pk": 7, "fields": {"app_label": "battDB", "model": "experimentalapparatus"}}, {"model": "contenttypes.contenttype", "pk": 8, "fields": {"app_label": "battDB", "model": "experiment"}}, {"model": "contenttypes.contenttype", "pk": 9, "fields": {"app_label": "battDB", "model": "cellbatch"}}, {"model": "contenttypes.contenttype", "pk": 10, "fields": {"app_label": "auth", "model": "permission"}}, {"model": "contenttypes.contenttype", "pk": 11, "fields": {"app_label": "auth", "model": "group"}}, {"model": "contenttypes.contenttype", "pk": 12, "fields": {"app_label": "auth", "model": "user"}}, {"model": "contenttypes.contenttype", "pk": 13, "fields": {"app_label": "contenttypes", "model": "contenttype"}}, {"model": "contenttypes.contenttype", "pk": 14, "fields": {"app_label": "admin", "model": "logentry"}}, {"model": "contenttypes.contenttype", "pk": 15, "fields": {"app_label": "sessions", "model": "session"}}, {"model": "contenttypes.contenttype", "pk": 16, "fields": {"app_label": "battDB", "model": "equipmenttype"}}, {"model": "contenttypes.contenttype", "pk": 17, "fields": {"app_label": "battDB", "model": "cellconfig"}}, {"model": "sessions.session", "pk": "n010godj6bb6o5rd2oicevkd37z7w8g8", "fields": {"session_data": "ODkzNGRjMTU3YjY1NTAxMDE2MGU5NGRmNzU3ZWQ1YjYzOGEwMGJjNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4ZDc3MzRjOGIwMDg0NmM4NGU3Nzg1ZGZiZjc3ZTk4ODBhMWE3OWFiIn0=", "expire_date": "2020-08-18T18:08:19.347Z"}}, {"model": "auth.permission", "pk": 1, "fields": {"name": "Can add cell", "content_type": 1, "codename": "add_cell"}}, {"model": "auth.permission", "pk": 2, "fields": {"name": "Can change cell", "content_type": 1, "codename": "change_cell"}}, {"model": "auth.permission", "pk": 3, "fields": {"name": "Can delete cell", "content_type": 1, "codename": "delete_cell"}}, {"model": "auth.permission", "pk": 4, "fields": {"name": "Can view cell", "content_type": 1, "codename": "view_cell"}}, {"model": "auth.permission", "pk": 5, "fields": {"name": "Can add cell separator", "content_type": 2, "codename": "add_cellseparator"}}, {"model": "auth.permission", "pk": 6, "fields": {"name": "Can change cell separator", "content_type": 2, "codename": "change_cellseparator"}}, {"model": "auth.permission", "pk": 7, "fields": {"name": "Can delete cell separator", "content_type": 2, "codename": "delete_cellseparator"}}, {"model": "auth.permission", "pk": 8, "fields": {"name": "Can view cell separator", "content_type": 2, "codename": "view_cellseparator"}}, {"model": "auth.permission", "pk": 9, "fields": {"name": "Can add equipment", "content_type": 3, "codename": "add_equipment"}}, {"model": "auth.permission", "pk": 10, "fields": {"name": "Can change equipment", "content_type": 3, "codename": "change_equipment"}}, {"model": "auth.permission", "pk": 11, "fields": {"name": "Can delete equipment", "content_type": 3, "codename": "delete_equipment"}}, {"model": "auth.permission", "pk": 12, "fields": {"name": "Can view equipment", "content_type": 3, "codename": "view_equipment"}}, {"model": "auth.permission", "pk": 13, "fields": {"name": "Can add manufacturer", "content_type": 4, "codename": "add_manufacturer"}}, {"model": "auth.permission", "pk": 14, "fields": {"name": "Can change manufacturer", "content_type": 4, "codename": "change_manufacturer"}}, {"model": "auth.permission", "pk": 15, "fields": {"name": "Can delete manufacturer", "content_type": 4, "codename": "delete_manufacturer"}}, {"model": "auth.permission", "pk": 16, "fields": {"name": "Can view manufacturer", "content_type": 4, "codename": "view_manufacturer"}}, {"model": "auth.permission", "pk": 17, "fields": {"name": "Can add signal type", "content_type": 5, "codename": "add_signaltype"}}, {"model": "auth.permission", "pk": 18, "fields": {"name": "Can change signal type", "content_type": 5, "codename": "change_signaltype"}}, {"model": "auth.permission", "pk": 19, "fields": {"name": "Can delete signal type", "content_type": 5, "codename": "delete_signaltype"}}, {"model": "auth.permission", "pk": 20, "fields": {"name": "Can view signal type", "content_type": 5, "codename": "view_signaltype"}}, {"model": "auth.permission", "pk": 21, "fields": {"name": "Can add test protocol", "content_type": 6, "codename": "add_testprotocol"}}, {"model": "auth.permission", "pk": 22, "fields": {"name": "Can change test protocol", "content_type": 6, "codename": "change_testprotocol"}}, {"model": "auth.permission", "pk": 23, "fields": {"name": "Can delete test protocol", "content_type": 6, "codename": "delete_testprotocol"}}, {"model": "auth.permission", "pk": 24, "fields": {"name": "Can view test protocol", "content_type": 6, "codename": "view_testprotocol"}}, {"model": "auth.permission", "pk": 25, "fields": {"name": "Can add experimental apparatus", "content_type": 7, "codename": "add_experimentalapparatus"}}, {"model": "auth.permission", "pk": 26, "fields": {"name": "Can change experimental apparatus", "content_type": 7, "codename": "change_experimentalapparatus"}}, {"model": "auth.permission", "pk": 27, "fields": {"name": "Can delete experimental apparatus", "content_type": 7, "codename": "delete_experimentalapparatus"}}, {"model": "auth.permission", "pk": 28, "fields": {"name": "Can view experimental apparatus", "content_type": 7, "codename": "view_experimentalapparatus"}}, {"model": "auth.permission", "pk": 29, "fields": {"name": "Can add experiment", "content_type": 8, "codename": "add_experiment"}}, {"model": "auth.permission", "pk": 30, "fields": {"name": "Can change experiment", "content_type": 8, "codename": "change_experiment"}}, {"model": "auth.permission", "pk": 31, "fields": {"name": "Can delete experiment", "content_type": 8, "codename": "delete_experiment"}}, {"model": "auth.permission", "pk": 32, "fields": {"name": "Can view experiment", "content_type": 8, "codename": "view_experiment"}}, {"model": "auth.permission", "pk": 33, "fields": {"name": "Can add cell batch", "content_type": 9, "codename": "add_cellbatch"}}, {"model": "auth.permission", "pk": 34, "fields": {"name": "Can change cell batch", "content_type": 9, "codename": "change_cellbatch"}}, {"model": "auth.permission", "pk": 35, "fields": {"name": "Can delete cell batch", "content_type": 9, "codename": "delete_cellbatch"}}, {"model": "auth.permission", "pk": 36, "fields": {"name": "Can view cell batch", "content_type": 9, "codename": "view_cellbatch"}}, {"model": "auth.permission", "pk": 37, "fields": {"name": "Can add permission", "content_type": 10, "codename": "add_permission"}}, {"model": "auth.permission", "pk": 38, "fields": {"name": "Can change permission", "content_type": 10, "codename": "change_permission"}}, {"model": "auth.permission", "pk": 39, "fields": {"name": "Can delete permission", "content_type": 10, "codename": "delete_permission"}}, {"model": "auth.permission", "pk": 40, "fields": {"name": "Can view permission", "content_type": 10, "codename": "view_permission"}}, {"model": "auth.permission", "pk": 41, "fields": {"name": "Can add group", "content_type": 11, "codename": "add_group"}}, {"model": "auth.permission", "pk": 42, "fields": {"name": "Can change group", "content_type": 11, "codename": "change_group"}}, {"model": "auth.permission", "pk": 43, "fields": {"name": "Can delete group", "content_type": 11, "codename": "delete_group"}}, {"model": "auth.permission", "pk": 44, "fields": {"name": "Can view group", "content_type": 11, "codename": "view_group"}}, {"model": "auth.permission", "pk": 45, "fields": {"name": "Can add user", "content_type": 12, "codename": "add_user"}}, {"model": "auth.permission", "pk": 46, "fields": {"name": "Can change user", "content_type": 12, "codename": "change_user"}}, {"model": "auth.permission", "pk": 47, "fields": {"name": "Can delete user", "content_type": 12, "codename": "delete_user"}}, {"model": "auth.permission", "pk": 48, "fields": {"name": "Can view user", "content_type": 12, "codename": "view_user"}}, {"model": "auth.permission", "pk": 49, "fields": {"name": "Can add content type", "content_type": 13, "codename": "add_contenttype"}}, {"model": "auth.permission", "pk": 50, "fields": {"name": "Can change content type", "content_type": 13, "codename": "change_contenttype"}}, {"model": "auth.permission", "pk": 51, "fields": {"name": "Can delete content type", "content_type": 13, "codename": "delete_contenttype"}}, {"model": "auth.permission", "pk": 52, "fields": {"name": "Can view content type", "content_type": 13, "codename": "view_contenttype"}}, {"model": "auth.permission", "pk": 53, "fields": {"name": "Can add log entry", "content_type": 14, "codename": "add_logentry"}}, {"model": "auth.permission", "pk": 54, "fields": {"name": "Can change log entry", "content_type": 14, "codename": "change_logentry"}}, {"model": "auth.permission", "pk": 55, "fields": {"name": "Can delete log entry", "content_type": 14, "codename": "delete_logentry"}}, {"model": "auth.permission", "pk": 56, "fields": {"name": "Can view log entry", "content_type": 14, "codename": "view_logentry"}}, {"model": "auth.permission", "pk": 57, "fields": {"name": "Can add session", "content_type": 15, "codename": "add_session"}}, {"model": "auth.permission", "pk": 58, "fields": {"name": "Can change session", "content_type": 15, "codename": "change_session"}}, {"model": "auth.permission", "pk": 59, "fields": {"name": "Can delete session", "content_type": 15, "codename": "delete_session"}}, {"model": "auth.permission", "pk": 60, "fields": {"name": "Can view session", "content_type": 15, "codename": "view_session"}}, {"model": "auth.permission", "pk": 61, "fields": {"name": "Can add equipment type", "content_type": 16, "codename": "add_equipmenttype"}}, {"model": "auth.permission", "pk": 62, "fields": {"name": "Can change equipment type", "content_type": 16, "codename": "change_equipmenttype"}}, {"model": "auth.permission", "pk": 63, "fields": {"name": "Can delete equipment type", "content_type": 16, "codename": "delete_equipmenttype"}}, {"model": "auth.permission", "pk": 64, "fields": {"name": "Can view equipment type", "content_type": 16, "codename": "view_equipmenttype"}}, {"model": "auth.permission", "pk": 65, "fields": {"name": "Can add cell config", "content_type": 17, "codename": "add_cellconfig"}}, {"model": "auth.permission", "pk": 66, "fields": {"name": "Can change cell config", "content_type": 17, "codename": "change_cellconfig"}}, {"model": "auth.permission", "pk": 67, "fields": {"name": "Can delete cell config", "content_type": 17, "codename": "delete_cellconfig"}}, {"model": "auth.permission", "pk": 68, "fields": {"name": "Can view cell config", "content_type": 17, "codename": "view_cellconfig"}}, {"model": "auth.user", "pk": 1, "fields": {"password": "pbkdf2_sha256$150000$2J7Bci8oeR8W$7IUeiZavNLMqx+xLNra875eCuEbiuXxpbFniRJl3kj0=", "last_login": "2020-08-04T18:08:19.312Z", "is_superuser": true, "username": "tom", "first_name": "", "last_name": "", "email": "", "is_staff": true, "is_active": true, "date_joined": "2020-08-04T18:08:06.798Z", "groups": [], "user_permissions": []}}, {"model": "admin.logentry", "pk": 1, "fields": {"action_time": "2020-08-04T18:13:10.226Z", "user": 1, "content_type": 9, "object_id": "1", "object_repr": "foo", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 2, "fields": {"action_time": "2020-08-04T18:25:35.516Z", "user": 1, "content_type": 4, "object_id": "1", "object_repr": "BorkCorp", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 3, "fields": {"action_time": "2020-08-04T18:26:04.905Z", "user": 1, "content_type": 9, "object_id": "1", "object_repr": "foo", "action_flag": 2, "change_message": "[{\"changed\": {\"fields\": [\"manufacturer\"]}}]"}}, {"model": "admin.logentry", "pk": 4, "fields": {"action_time": "2020-08-04T18:27:53.921Z", "user": 1, "content_type": 2, "object_id": "1", "object_repr": "MyMembrane", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 5, "fields": {"action_time": "2020-08-04T18:28:19.927Z", "user": 1, "content_type": 1, "object_id": "1", "object_repr": "MyLiPo", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 6, "fields": {"action_time": "2020-08-04T18:41:57.989Z", "user": 1, "content_type": 4, "object_id": "2", "object_repr": "Maccor", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 7, "fields": {"action_time": "2020-08-04T18:42:29.857Z", "user": 1, "content_type": 16, "object_id": "1", "object_repr": "GalvoTron 3000", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 8, "fields": {"action_time": "2020-08-04T18:45:01.780Z", "user": 1, "content_type": 16, "object_id": "2", "object_repr": "GalvoTron 3000", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 9, "fields": {"action_time": "2020-08-04T18:47:34.828Z", "user": 1, "content_type": 3, "object_id": "1", "object_repr": "Tom's GalvoTron 3000", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 10, "fields": {"action_time": "2020-08-04T18:51:08.397Z", "user": 1, "content_type": 6, "object_id": "1", "object_repr": "PyBaMM example protocol", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 11, "fields": {"action_time": "2020-08-04T18:52:01.270Z", "user": 1, "content_type": 7, "object_id": "1", "object_repr": "Tom's Lab", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 12, "fields": {"action_time": "2020-08-04T18:52:35.233Z", "user": 1, "content_type": 16, "object_id": "1", "object_repr": "GalvoTron 3000", "action_flag": 3, "change_message": ""}}, {"model": "admin.logentry", "pk": 13, "fields": {"action_time": "2020-08-04T18:52:52.127Z", "user": 1, "content_type": 3, "object_id": "1", "object_repr": "Tom's GalvoTron 3000", "action_flag": 2, "change_message": "[{\"changed\": {\"fields\": [\"type\"]}}]"}}, {"model": "admin.logentry", "pk": 14, "fields": {"action_time": "2020-08-04T18:54:28.563Z", "user": 1, "content_type": 8, "object_id": "1", "object_repr": "Experiment object (1)", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 15, "fields": {"action_time": "2020-08-04T19:17:17.174Z", "user": 1, "content_type": 17, "object_id": "1", "object_repr": "4s", "action_flag": 1, "change_message": "[{\"added\": {}}]"}}, {"model": "admin.logentry", "pk": 16, "fields": {"action_time": "2020-08-04T19:26:50.203Z", "user": 1, "content_type": 8, "object_id": "1", "object_repr": "test test", "action_flag": 2, "change_message": "[{\"changed\": {\"fields\": [\"cells\", \"processed_data_file\"]}}]"}}, {"model": "admin.logentry", "pk": 17, "fields": {"action_time": "2020-08-04T19:36:45.200Z", "user": 1, "content_type": 8, "object_id": "1", "object_repr": "test test", "action_flag": 2, "change_message": "[{\"changed\": {\"fields\": [\"raw_data_file\", \"processed_data_file\"]}}]"}}, {"model": "battDB.experiment", "pk": 1, "fields": {"attributes": {}, "name": "test test", "owner": 1, "date": "2020-08-04", "apparatus": 1, "raw_data_file": "raw_data_files/MT6735M_Android_scatter.txt", "processed_data_file": "processed_data_files/Pump.io_Logo.svg", "parameters": {"EndVoltage": null, "StartVoltage": null}, "analysis": {"MeasuredCapacity": null, "MeasuredResistance": null}, "cells": [1]}}]