import requests
import urllib.parse

# 读取 .tex 文件内容
with open('main.tex', 'r', encoding='utf-8') as file:
    tex_content = file.read()

# 对内容进行 URL 编码
encoded_tex_content = urllib.parse.quote(tex_content)

# 设置 API 端点
api_endpoint = f'http://latexonline.cc/compile?text={encoded_tex_content}'

# 发送请求并保存生成的 PDF
response = requests.get(api_endpoint)
if response.status_code == 200:
    with open('output.pdf', 'wb') as f:
        f.write(response.content)
    print("PDF successfully generated and saved as output.pdf")
else:
    print(f"Failed to compile LaTeX. Status code: {response.status_code}")
