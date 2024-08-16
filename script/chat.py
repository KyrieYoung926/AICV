import openai

# 设置 API 密钥
openai.api_key = 'sk-VkA537f9bc0eb7889e1299ef80824339ebbf05469c3xZBrh'

# 定义请求的参数
model = "gpt-4o-mini"  # 或者 "gpt-4"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello! How do I use the ChatGPT API in Python?"}
]

# 调用 ChatGPT API 生成聊天完成
response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    max_tokens=150,  # 生成的最大 tokens 数量
    temperature=0.7,  # 控制生成文本的随机性
    top_p=1.0,  # 样本中的核选择
    n=1,  # 生成多少个响应
    frequency_penalty=0,  # 控制模型重复字词的倾向
    presence_penalty=0  # 控制模型引入新话题的倾向
)

# 输出生成的聊天完成
print(response['choices'][0]['message']['content'])
