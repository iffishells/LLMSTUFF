from setuptools import setup, find_packages

setup(
    name="ChatToBooks",
    version="0.0",
    packages=find_packages(where="app"),  # assuming source code is in the app directory
    package_dir={"": "app"},  # maps the package directory
    install_requires=[
        # List your dependencies here
        # e.g., 'numpy', 'requests',
    ],
    description="A chatbot application",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/yourproject",
)
