"""
多语言示例

此示例展示如何使用 structured_output_prompt 库生成不同语言的结构化输出提示词。
"""

import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from pydantic import BaseModel, Field
from structured_output_prompt import generate_structured_prompt


# 定义一个简单的 Pydantic 模型
class Product(BaseModel):
    name: str = Field(description="The product name")
    price: float = Field(description="The product price")
    category: str = Field(description="The product category")


def main():
    # 生成不同语言的默认模板提示词
    languages = ["zh", "en", "ja", "de", "fr"]

    for lang in languages:
        prompt = generate_structured_prompt(Product, language=lang, template="default")
        print(f"{lang.upper()} 模板提示词：")
        print(prompt)
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
