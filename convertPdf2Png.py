from pdf2image import convert_from_path

def convert_pdf_to_png(pdf_path, output_prefix):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        output_path = f"{output_prefix}{i+1}.png"
        image.save(output_path, "PNG")

# 指定输入的PDF文件路径和输出的图片前缀
pdf_file = "input.pdf"
output_prefix = "output"

# 调用函数进行转换
convert_pdf_to_png(pdf_file, output_prefix)
