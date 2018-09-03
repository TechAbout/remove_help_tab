# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "remove_help_tab"
app_title = "Remove Help Tab"
app_publisher = "Jazib Zaman"
app_description = "Remove Help Tab from top menu"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "jazib@wparena.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/remove_help_tab/css/logo_modify.css"
app_include_js = "/assets/remove_help_tab/js/remove_help_tab.js"
# app_include_js = "/assets/remove_help_tab/js/remove_learn_module.js"

# include js, css files in header of web template
# web_include_css = "/assets/remove_help_tab/css/remove_help_tab.css"
# web_include_js = "/assets/remove_help_tab/js/remove_help_tab.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "remove_help_tab.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "remove_help_tab.install.before_install"
# after_install = "remove_help_tab.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "remove_help_tab.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"remove_help_tab.tasks.all"
# 	],
# 	"daily": [
# 		"remove_help_tab.tasks.daily"
# 	],
# 	"hourly": [
# 		"remove_help_tab.tasks.hourly"
# 	],
# 	"weekly": [
# 		"remove_help_tab.tasks.weekly"
# 	]
# 	"monthly": [
# 		"remove_help_tab.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "remove_help_tab.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "remove_help_tab.event.get_events"
# }

