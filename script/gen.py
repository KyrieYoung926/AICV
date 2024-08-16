from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

def create_pdf():
    # 创建文档对象
    doc = Document()

    # 添加内容
    with doc.create(Section('Introduction')):
        doc.append('This is the first section.')
        with doc.create(Subsection('A subsection')):
            doc.append(italic('Some italic text.'))

    # 生成 PDF 文件
    doc.generate_pdf('output', clean_tex=False)

# 生成示例 PDF
create_pdf()
