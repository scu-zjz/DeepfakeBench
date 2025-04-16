from setuptools import setup, find_packages



"""
For documentations, see here:
https://github.com/pypa/sampleproject/blob/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.py

在工作路径下运行下列指令：
pip install -e .  
即可实现本地安装本包，并在更新文件时自动更新相应内容，便于调试开发。
"""

def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

def requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements

# exit(0)

setup(
    name='deepfakebench',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements(),
)
