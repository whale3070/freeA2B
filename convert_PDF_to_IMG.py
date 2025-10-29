import fitz  # PyMuPDF
#pip install pymupdf
def convert_pdf_to_png(pdf_path, output_prefix):
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        # 设置分辨率（dpi 越高图片越清晰）
        zoom = 2.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        output_path = f"{output_prefix}{i+1}.png"
        pix.save(output_path)
    doc.close()

convert_pdf_to_png("input.pdf", "output")
