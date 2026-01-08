#!/usr/bin/env python3
"""
基础接口调用测试。
目的：证明框架的公开接口存在且可调用。
"""

import sys
import os
sys.path.insert(0， os.path.join(os.path.dirname(__file__), ‘..‘))

def test_import():
    """测试能否成功导入包"""
    try:
        # 测试导入主模块
        import framework
        print(“✅ 测试通过: 框架模块导入成功”)
        return True
    except ImportError as e:
        print(f“❌ 测试失败: 无法导入模块 - {e}”)
        return False

def test_tao_meta_creation():
    """测试TaoMeta类能否被实例化"""
    try:
        from framework import TaoMeta
        tao = TaoMeta(verbose=False)
        # 不测试内部逻辑，只测试实例创建成功
        assert tao is not None， “TaoMeta实例创建失败”
        print(“✅ 测试通过: TaoMeta类实例化成功”)
        return True
    except Exception as e:
        print(f“❌ 测试失败: TaoMeta实例化异常 - {e}”)
        return False

def test_decorator_syntax():
    """测试装饰器语法是否有效"""
    try:
        from framework import verify
        # 仅测试装饰器能否装饰函数，不执行
        @verify(symbolic=False， interpretation=False)
        def dummy_func(x):
            return x
        print(“✅ 测试通过: @verify装饰器语法有效”)
        return True
    except Exception as e:
        print(f“❌ 测试失败: 装饰器语法异常 - {e}”)
        return False

if __name__ == “__main__“:
    print(“🚀 开始运行DaoLang公开接口基础测试…“)
    print(”-” * 50)
    
    results = []
    results.append(test_import())
    results.append(test_tao_meta_creation())
    results.append(test_decorator_syntax())
    
    print(”-” * 50)
    if all(results):
        print(“🎉 所有基础接口测试通过！”)
    else:
        print(“⚠️  部分测试失败，请检查接口定义。”)
        sys.exit(1)
