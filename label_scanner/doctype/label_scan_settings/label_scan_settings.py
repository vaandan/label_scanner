from frappe.model.document import Document

class LabelScanSettings(Document):
    def validate(self):
        self.validate_patterns()
    
    def validate_patterns(self):
        import re
        try:
            re.compile(self.batch_pattern)
            re.compile(self.serial_pattern)
            re.compile(self.quantity_pattern)
        except re.error:
            frappe.throw(_("Invalid regular expression pattern"))
