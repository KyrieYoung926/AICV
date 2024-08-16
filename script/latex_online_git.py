import requests

# 原始 URL，注意这里需要使用原始文件内容的链接
tex_file_url = 'https://github.com/KyrieYoung926/AICV/blob/main/texs/main.tex'

# LaTeX 编译 API 的 URL
api_endpoint = f'http://latexonline.cc/compile?url={tex_file_url}'

# 发送 GET 请求到 LaTeX 编译 API
response = requests.get(api_endpoint)

# 处理响应
if response.status_code == 200:
    with open('output.pdf', 'wb') as f:
        f.write(response.content)
    print("PDF successfully generated and saved as output.pdf")
else:
    print(f"Failed to compile LaTeX. Status code: {response.status_code}")
    print(response.text)
