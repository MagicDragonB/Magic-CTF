import hashlib

# 指定文件的完整路径
file_path = r"D:\Website Download Default File\cheese_list.txt"

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    cheese_list = [line.strip() for line in file.readlines() if line.strip()]

# 计算并输出每个奶酪的哈希值
print("奶酪名称及其SHA-256哈希值：")
print("-" * 70)
for cheese in cheese_list:
    hash_hex = hashlib.sha256(cheese.encode()).hexdigest()
    print(f"{cheese.ljust(40)} | {hash_hex}")

# 可选：额外检查是否以 "50ca" 结尾
target_suffix = "50ca"
matching_cheeses = [
    (cheese, hash_hex)
    for cheese in cheese_list
    if hashlib.sha256(cheese.encode()).hexdigest().endswith(target_suffix)
]

if matching_cheeses:
    print("\n以下奶酪名称的哈希值以 '50ca' 结尾：")
    for cheese, hash_hex in matching_cheeses:
        print(f"- {cheese} (哈希值: ...{hash_hex[-4:]})")
else:
    print("\n没有找到哈希值以 '50ca' 结尾的奶酪名称。")