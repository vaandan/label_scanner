import frappe
import base64
import pytesseract
from PIL import Image
import io
import re

@frappe.whitelist()
def process_label_image(image_data):
    try:
        # Remove the data URL prefix
        image_data = image_data.split(',')[1]
        
        # Decode base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Extract text using pytesseract
        extracted_text = pytesseract.image_to_string(image)
        
        # Get label scan settings
        settings = frappe.get_doc('Label Scan Settings')
        
        # Extract batch number
        batch_match = re.search(settings.batch_pattern, extracted_text)
        batch_no = batch_match.group(1) if batch_match else None
        
        # Extract serial numbers
        serial_matches = re.findall(settings.serial_pattern, extracted_text)
        serial_nos = serial_matches if serial_matches else []
        
        # Extract quantity
        qty_match = re.search(settings.quantity_pattern, extracted_text)
        qty = float(qty_match.group(1)) if qty_match else 1
        
        return {
            'batch_no': batch_no,
            'serial_nos': serial_nos,
            'qty': qty
        }
    except Exception as e:
        frappe.log_error(f"Label Scanner Error: {str(e)}")
        frappe.throw(f"Error processing image: {str(e)}")