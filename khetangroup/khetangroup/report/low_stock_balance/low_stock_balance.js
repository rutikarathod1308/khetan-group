// Copyright (c) 2023, rutika and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Low Stock Balance"] = {
	"filters": [

	],
	"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		if (column.fieldname == "qty" && data && data.qty > 0) {
			value = "<span style='color:red'>" + value + "</span>";
		}
		return value ;
	},
};
