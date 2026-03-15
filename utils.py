# utils.py
import tempfile
import os
from markitdown import MarkItDown

def extract_text(uploaded_file):
    """
    Universally extracts text from diverse file types using MarkItDown.
    """
    suffix = os.path.splitext(uploaded_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    
    try:
        md = MarkItDown()
        result = md.convert(tmp_path)
        return result.text_content
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)