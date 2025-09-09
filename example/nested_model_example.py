"""
嵌套模型示例

此示例展示如何使用 structured_output_prompt 库处理嵌套 Pydantic 模型。
"""

import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from pydantic import BaseModel, Field
from typing import List
from structured_output_prompt import generate_structured_prompt


# 定义嵌套模型
class Address(BaseModel):
    street: str = Field(description="The street address")
    city: str = Field(description="The city")
    zip_code: str = Field(description="The zip code")


class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age")
    addresses: List[Address] = Field(description="List of addresses")


def main():
    # 生成嵌套模型的提示词
    prompt = generate_structured_prompt(Person, language="zh", template="default")
    print("嵌套模型提示词：")
    print(prompt)
    print("\n" + "=" * 50 + "\n")

    # 生成纯模型描述
    prompt_none = generate_structured_prompt(Person, template=None)
    print("嵌套模型纯描述：")
    print(prompt_none)


if __name__ == "__main__":
    main()
