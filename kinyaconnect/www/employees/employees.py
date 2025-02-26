import frappe

def get_context(context):
    context.employees = frappe.get_all(
        "Employee",
        fields=["Full Name", "Role", "Image"]
    )
    return context