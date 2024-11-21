frappe.provide('label_scanner');

label_scanner.capture_image = function() {
    let input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.capture = 'environment';
    
    input.onchange = function() {
        let file = input.files[0];
        let reader = new FileReader();
        
        reader.onload = function(e) {
            frappe.show_alert({
                message: __('Processing image...'),
                indicator: 'blue'
            });
            
            frappe.call({
                method: 'label_scanner.api.process_label_image',
                args: {
                    image_data: e.target.result
                },
                callback: function(r) {
                    if (!r.exc) {
                        frappe.show_alert({
                            message: __('Image processed successfully'),
                            indicator: 'green'
                        });
                        label_scanner.update_fields(r.message);
                    }
                }
            });
        };
        reader.readAsDataURL(file);
    };
    input.click();
};

label_scanner.update_fields = function(data) {
    if (!cur_frm) return;
    
    let item = cur_frm.doc.items[0];
    if (!item) {
        cur_frm.add_child('items', {});
        item = cur_frm.doc.items[0];
    }
    
    if (data.batch_no) item.batch_no = data.batch_no;
    if (data.serial_nos) item.serial_no = data.serial_nos.join('\n');
    if (data.qty) item.qty = data.qty;
    
    cur_frm.refresh_field('items');
};