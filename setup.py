
#### 2. **setup.py**


from setuptools import setup, find_packages

setup(
    name="gerador_ficha_olddragon",
    version="1.0.0",
    author="Luciano de Castro",
    author_email="lcm_cefet@hotmail.com",
    description="Gerador de fichas de personagens para o sistema Old Dragon",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lcm2025/cria-o-de-ficha-OLDDRAGON",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)