frappe.ui.form.on('Label Scan Settings', {
    refresh: function(frm) {
        frm.add_custom_button(__('Test Scanner'), function() {
            label_scanner.capture_image();
        });
    }
});