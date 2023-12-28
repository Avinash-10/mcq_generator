from setuptools import find_packages,setup

setup(
    name = "mcq_generator",
    version = "0.0.1",
    author = "Avinash-10",
    author_email = "avinash1999.vyas@gmail.com",
    install_requirements = ["openai","langchain","streamlit","python-dotenv","PyPDF2","pandas"],
    packages = find_packages()
)