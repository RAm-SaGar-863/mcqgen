from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='ram sagar',
    author_email="ramsagarkaduthuri@gmail.com",
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2","huggingface_hub","transformers","accelerate","bitsandbytes"],
    packages=find_packages()
)