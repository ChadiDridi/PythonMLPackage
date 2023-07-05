from setuptools import find_packages, setup, find_namespace_packages

required_packages = [
    'numpy',
    'pandas',
    'matplotlib',
    'seaborn',
    'scikit-learn',
    'scipy',
    'tensorflow',
    'keras',
    'seaborn',
    'statsmodels',
    'xgboost',
    'lightgbm',
    'catboost',
    'tensorflow-addons',
    'imbalanced-learn',
    'mlxtend',
    'pydot',
    'graphviz',
    'pytorch',
    'pytorch-lightning',
    'pytorch-ignite',
    'pytorch-forecasting',
    'tensorflow-probability',
    'tensorflow-datasets',
    'pybrain',
    'scrapy',
    'pandas',
    'gekko',
    'pymc3',
    'opencv-python',
    'opencv-contrib-python',
    'torch',
    'tclab',
]

# Packages that are not available on PyPI
problematic_packages = [
    'pytorch-quantum',
    'pytorch-forecasting',
    'pytorch-tabnet',
    'transfer-learning-conv-3d',
    'transfer-learning-conv-2d',
    'transfer-learning-lstm',
    'transfer-learning-vgg19',
    'beautifulsupe4',
    'gekko',
    'pymc3',
    'tclab',
]

# Check if a problematic package is available before installing
for package in problematic_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Warning: The '{package}' package is not installed.")

setup(
    name="chady",
    version="0.2",
    description="A package for ML libraries",
    author="Chadi",
    author_email="dridichady@gmail.com",
    url="https://github.com/ChadiDridi/PythonMLPackage",
    packages=find_packages(),
    install_requires=required_packages,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License Audience :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
