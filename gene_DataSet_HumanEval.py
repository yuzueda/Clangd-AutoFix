import openai
import json

openai.api_key = 'your-api-key'

def generate_code(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=256,
        temperature=0.2,
        stop=["\n\n"]
    )
    return response.choices[0].text.strip()

# 读取 HumanEval-X 数据
with open('humaneval_x.jsonl', 'r') as f:
    data = [json.loads(line) for line in f]

# 生成代码并保存
samples = []
for item in data:
    code = generate_code(item['prompt'])
    samples.append({
        "task_id": item["task_id"],
        "generation": code
    })

# 保存生成结果
with open('samples.jsonl', 'w') as f:
    for sample in samples:
        f.write(json.dumps(sample) + '\n')
