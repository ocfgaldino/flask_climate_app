from setuptools import setup, find_packages
# find_packages ---> every folder with __init__.py will be considered as a package to be described to this app.

def read(filename):
    return [
        req.strip()
        for req in 
        open(filename).readlines()
        
    ]



setup(
    name = "Flask_Climate",
    version = "0.1.0", # major, minor, patch
    description = "Web app to explore the Inmet Data (Brazil)",
    #packages = ['flask_climate',]
    packages=find_packages(),
    include_package_data=True, # metadata 
    install_requires=read("requirements.txt"),
    extra_require={
        "dev": read("requirements-dev.txt")
    }    
)