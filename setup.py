from setuptools import setup

setup(
    name="subtitlematcher",
    version="1.0.0",
    description="Matching video and subtitle file name",
    url="http://github.com/itsjef/subtitlematcher",
    author="Duc Anh Tran",
    author_email="td.anh0812@gmail.com",
    license='MIT',
    packages=["subtitlematcher"],
    scripts=["src/subtitlematcher"],
    zip_safe=False
)
