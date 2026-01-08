#!/usr/bin/env python3
"""
演示集成测试。
目的：证明框架能与演示代码正常协同工作。
"""

import sys
import os
import subprocess

def run_demo_and_check(demo_script):
    """运行演示脚本并检查是否正常退出（不校验具体输出）"""
    try:
        # 仅检查演示能否运行完成，不校验业务逻辑
        result = subprocess.run(
            [sys.executable， demo_script]，
            cwd=os.path.join(os.path.dirname(__file__), ‘..‘)，
            capture_output=True，
            text=True，
            timeout=30
        )
        if result.returncode == 0:
            print(f“✅ 测试通过: 演示脚本 `{demo_script}` 运行完成”)
            return True
        else:
            print(f“❌ 测试失败: `{demo_script}` 运行出错”)
            print(f“   错误输出: {result.stderr[:200]}”) # 仅截取部分错误信息
            return False
    except subprocess.TimeoutExpired:
        print(f“❌ 测试失败: `{demo_script}` 运行超时”)
        return False
    except Exception as e:
        print(f“❌ 测试失败: 运行 `{demo_script}` 时发生异常 - {e}”)
        return False

if __name__ == “__main__“:
    print(“🚀 开始运行DaoLang演示集成测试…“)
    print(”-” * 50)
    
    demos_to_test = [
        “demos/demo_showcase.py”，
    ]
    
    results = []
    for demo in demos_to_test:
        demo_path = os.path.join(‘..‘， demo)
        if os.path.exists(demo_path):
            results.append(run_demo_and_check(demo_path))
        else:
            print(f“⚠️  跳过: 演示文件 `{demo}` 不存在”)
    
    print(”-” * 50)
    if all(results):
        print(“🎉 所有演示集成测试通过！”)
    else:
        print(“⚠️  部分演示运行失败。”)
        sys.exit(1)
