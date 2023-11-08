# Copyright (c) 2023, rutika and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns(filters)
	data = []
	items_detail = item_details(filters)
	for items_details in items_detail:
		data.append({
			"item_code":items_details.item_code,
			"warehouse":items_details.warehouse,
			"qty":items_details.actual_qty,
			"safety_qty":items_details.safety_stock
       
		})
	return columns, data


def get_columns (filters):
    column = [
		{
			"label":_("Item Code"),
			"fieldname":"item_code",
			"fieldtype":"Link",
			"options":"Item"
		},
  {
			"label":_("Warehouse"),
			"fieldname":"warehouse",
			"fieldtype":"Link",
			"options":"Warehouse"
		},
  {
			"label":_("Safety Qty"),
			"fieldname":"safety_qty",
			"fieldtype":"Float"
		},
  {
			"label":_("Qty"),
			"fieldname":"qty",
			"fieldtype":"Float"
		},
  
	]
    return column

def item_details (filters):
    query = (f""" 
             select  item.item_code, se.warehouse, bin.actual_qty, se.safety_stock from `tabItem` item join `tabSafety Stock` se on item.name = se.parent
             join `tabBin` bin on item.item_code = bin.item_code
             where item.disabled = 0
             and
             se.warehouse = bin.warehouse
             and 
             bin.actual_qty < se.safety_stock
             """)
    main_query = frappe.db.sql(query, as_dict=True)
    return main_query