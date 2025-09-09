"""
基本使用示例

此示例展示如何使用 structured_output_prompt 库生成基本的结构化输出提示词。
"""

import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from pydantic import BaseModel, Field
from structured_output_prompt import generate_structured_prompt


# 定义一个简单的 Pydantic 模型
class User(BaseModel):
    name: str = Field(description="用户的全名")
    age: int = Field(description="用户的年龄")
    email: str = Field(description="用户的电子邮件地址")


def main():
    # 生成中文默认模板的提示词
    prompt = generate_structured_prompt(User, language="zh", template="default")
    print("中文默认模板提示词：")
    print(prompt)
    print("\n" + "=" * 50 + "\n")

    # 生成纯模型描述（无模板）
    prompt_none = generate_structured_prompt(User, template=None)
    print("纯模型描述：")
    print(prompt_none)


if __name__ == "__main__":
    main()
