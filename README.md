# ChemiPy 🧪

Welcome to the ChemiPy repository! ChemiPy is a Python toolkit designed to assist you in various aspects of chemistry, from electron configurations to molecular calculations.

## Features 📚

### 1. Electron Configuration Formatter 🌐

The `electron_configuration_stable` function takes an atomic number as input and provides a stable electron configuration. It also handles exceptions for elements like Chromium (Cr) and Copper (Cu).

### 2. Electron Configuration Formatter with Superscripts 🧾

The `format_electron_configuration` function enhances the readability of electron configurations by using superscripts to denote the number of electrons in each sublevel.

### 3. (Add more features here as you develop them)

## Usage 🛠️

To use ChemiPy, simply include the relevant functions from the `chemipy.py` file in your Python project. You can then call these functions with the appropriate parameters.

```python
from chemipy import electron_configuration_stable, format_electron_configuration

# Example usage
atomic_number = 29
config = electron_configuration_stable(atomic_number)
formatted_config = format_electron_configuration(config)
print(f'Stable Electron configuration for atomic number {atomic_number}: {formatted_config}')
```

## Code Output Example 🚀

When you run the example code provided, you will get an output like this:

```
Stable Electron configuration for atomic number 29 (Copper): 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d¹⁰
```
**Repository Views** ![Views](https://profile-counter.glitch.me/Chemipy/count.svg)


## Contributions 🤝

Contributions are welcome! If you have ideas for additional features or improvements, please feel free to open an issue or submit a pull request.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding and exploring the world of chemistry with ChemiPy! 🌟🧪
