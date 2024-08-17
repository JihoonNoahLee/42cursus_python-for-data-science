# ft_package

This is the `ft_package` repository, which contains count_in_list function.

## Installation

To install the `ft_package`, simply clone this repository to your local machine and build using pip.

```bash
git clone https://github.com/JihoonNoahLee/42cursus_python-for-data-science.git
cd 0-starting/ex09

# Use One of three following:
pip install .
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

Once you have cloned the repository, you can import the functions from the `ft_package` module into your Python scripts or notebooks:

```python
from ft_package import count_in_list

# Example usage
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.
