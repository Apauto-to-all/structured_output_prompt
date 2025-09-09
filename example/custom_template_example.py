"""
自定义模板示例

此示例展示如何使用 structured_output_prompt 库生成自定义模板的结构化输出提示词。
"""

import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from pydantic import BaseModel, Field
from structured_output_prompt import generate_structured_prompt


# 定义一个简单的 Pydantic 模型
class Order(BaseModel):
    order_id: int = Field(description="订单ID")
    customer_name: str = Field(description="客户姓名")
    total_amount: float = Field(description="订单总金额")


def main():
    # 使用自定义模板
    custom_template = (
        "请根据以下模型结构生成 JSON 数据：\n{model_desc}\n确保输出为有效 JSON。"
    )

    prompt = generate_structured_prompt(Order, language="zh", template=custom_template)
    print("自定义模板提示词：")
    print(prompt)
    print("\n" + "=" * 50 + "\n")

    # 另一个自定义模板示例
    custom_template2 = (
        "Output the following in JSON format:\n{model_desc}\nNo additional text."
    )

    prompt2 = generate_structured_prompt(
        Order, language="en", template=custom_template2
    )
    print("英文自定义模板提示词：")
    print(prompt2)


if __name__ == "__main__":
    main()
