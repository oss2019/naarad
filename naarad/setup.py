import setuptools
import find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='naarad',
     version='0.1',
     scripts=['naarad'],
     author="Harshit Jain",
     author_email="harshitjain1309@gmail.com",
     description="""The chivalrous messenger god is here to reduce your burden
     of Digital Publicity of your college events in facebook groups.""",
     long_description=open("README.md").read(),
     long_description_content_type="text/markdown",
     url="https://github.com/oss2019/naarad",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     include_package_data=True
 )
