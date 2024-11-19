source_link = "https://github.com/yourusername/label_scanner"
docs_base_url = "https://yourusername.github.io/label_scanner"
headline = "OCR Label Scanner for ERPNext"
sub_heading = "Scan labels to automatically fill Purchase Receipt details"

def get_context(context):
    context.brand_html = "Label Scanner"
    context.source_link = source_link
    context.docs_base_url = docs_base_url
    context.headline = headline
    context.sub_heading = sub_heading
    return context