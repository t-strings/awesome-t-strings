# Awesome T-Strings [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A curated list of resources, tools, libraries, and examples for Python's Template Strings (t-strings) introduced in Python 3.14

> [!WARNING]
> Template strings are currently in **beta** as part of Python 3.14. The syntax and behavior may change before the final release. This feature is experimental and should not be used in production code yet.

Template strings (t-strings) are a powerful new Python feature defined in [PEP 750](https://peps.python.org/pep-0750/) that extends f-strings with programmable string processing capabilities. They enable safer string interpolation, prevent injection attacks, and allow for custom domain-specific languages.

## Contents

- [What are T-Strings?](#what-are-t-strings)
- [Official Resources](#official-resources)
- [Development Tools](#development-tools)
  - [Linting & Static Analysis](#linting--static-analysis)
  - [Type Checking](#type-checking)
  - [IDE Extensions](#ide-extensions)
  - [Environment & Installation](#environment--installation)
- [Libraries & Frameworks](#libraries--frameworks)
  - [Database & SQL](#database--sql)
  - [Utilities](#utilities)
- [Learning Resources](#learning-resources)
  - [Tutorials & Videos](#tutorials--videos)
  - [Community Discussions](#community-discussions)
- [Getting Started](#getting-started)
- [Related](#related)
- [Contributing](#contributing)

## What are T-Strings?

Template strings (t-strings) are a new Python feature that provide programmable string interpolation. Unlike f-strings which immediately produce a string, t-strings return a structured template object that can be processed by custom functions. This enables:

- **Security**: Prevent injection attacks through controlled processing
- **Flexibility**: Create custom DSLs for any domain (SQL, HTML, logging, etc.)
- **Performance**: Lazy evaluation and optimized string handling
- **Type Safety**: Full static type checking support

### Basic Examples (from PEP 750)

```python
# Template strings use 't' prefix instead of 'f'
template: Template = t"Hello {name}"

# HTML auto-escaping example
evil = "<script>alert('evil')</script>"
template = t"<p>{evil}</p>"
assert html(template) == "<p>&lt;script&gt;alert('evil')&lt;/script&gt;</p>"

# HTML attributes from dictionary
attributes = {"src": "shrubbery.jpg", "alt": "looks nice"}
template = t"<img {attributes} />"
assert html(template) == '<img src="shrubbery.jpg" alt="looks nice" />'

# Accessing template components
name = "World"
template = t"Hello {name}"
assert template.strings == ("Hello ", "")
assert template.interpolations[0].value == "World"
assert template.interpolations[0].expression == "name"
```

Learn more in [PEP 750](https://peps.python.org/pep-0750/).

## Official Resources

- [PEP 750: Template Strings](https://peps.python.org/pep-0750/) - The official specification defining t-strings syntax and semantics
- [Python 3.14.0b2](https://www.python.org/downloads/release/python-3140b2/) - Python beta release with t-strings support (⚠️ Experimental)
- [t-strings.help](https://t-strings.help/) - Documentation and help site maintained by the PEP 750 author

## Development Tools

### Linting & Static Analysis

- [t-linter](https://github.com/koxudaxi/t-linter) - Comprehensive linting tool for t-strings with IDE integrations
  - [PyPI Package](https://pypi.org/project/t-linter/) - `pip install t-linter`

### Type Checking

- [Pyright with t-strings support](https://github.com/koxudaxi/pyright/releases/tag/1.1.401-pep750.1) - Fork of Pyright with full t-strings type checking support

### IDE Extensions

- [VS Code T-Linter](https://marketplace.visualstudio.com/items?itemName=koxudaxi.t-linter) - Syntax highlighting, linting, and IntelliSense for t-strings
- [PyCharm T-Linter Plugin](https://plugins.jetbrains.com/plugin/27541-tlinter) - Full IDE support for JetBrains products ([Source](https://github.com/koxudaxi/t-linter-pycharm-plugin))

### Environment & Installation

- [uv](https://github.com/astral-sh/uv) - Fast Python package manager with built-in Python version management
- [Python Docker Images](https://hub.docker.com/_/python) - Official Python images (3.14-rc tags available)
- [CPython Source](https://github.com/python/cpython/tree/v3.14.0b2) - Build Python 3.14 from source

## Libraries & Frameworks

### Database & SQL

- [sql-tstring](https://github.com/pgjones/sql-tstring) - Safe SQL query building with t-strings, preventing SQL injection
  - [PyPI Package](https://pypi.org/project/sql-tstring/) - `pip install sql-tstring`
  - Features parameterized queries, type safety, and database adapter integration

### Utilities

- [better-dedent](https://github.com/treyhunner/better-dedent) - Enhanced string dedenting for cleaner template formatting

## Learning Resources

### Tutorials & Videos

- [Python Template Strings Introduction](https://www.youtube.com/watch?v=yx1QPm4aXeA) - Video tutorial on t-strings basics
- [Template Strings Advanced Usage](https://www.youtube.com/watch?v=WCWNeZ_rE68) - Advanced patterns and use cases

### Community Discussions

- [Language hints for PEP 750](https://discuss.python.org/t/language-hints-for-pep-750-template-strings/94311/) - Discussion on syntax highlighting and language detection
- [PEP 750 template strings new updates](https://discuss.python.org/t/pep750-template-strings-new-updates/71594) - Latest updates and changes to the specification
- [Template strings in stdlib logging](https://discuss.python.org/t/add-support-for-t-strings-in-the-stdlib-logging-library/92776/23) - Integration with Python's logging module
- [Original PEP 750 discussion](https://discuss.python.org/t/pep-750-tag-strings-for-writing-domain-specific-languages/60408) - Initial proposal and community feedback
- [Convert function for string.Template](https://discuss.python.org/t/add-convert-function-to-string-templatelib/94569) - Bridging classic templates with t-strings


## Getting Started

### Installation

To start using t-strings, you'll need Python 3.14 or later:

```bash
# Using uv package manager
uv python install 3.14

# Using Docker
docker run -it python:3.14-rc

# Build from source
git clone https://github.com/python/cpython.git
cd cpython
git checkout v3.14.0b2
./configure --enable-optimizations
make -j4  # Or use $(nproc) on Linux, $(sysctl -n hw.ncpu) on macOS
sudo make altinstall
```


## Related

- [PEP 787: Safer Subprocess Usage](https://peps.python.org/pep-0787/) - Using t-strings for secure subprocess command execution
- [Python f-strings](https://peps.python.org/pep-0498/) - The predecessor to t-strings
- [Template Literal (JavaScript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) - Similar concept in JavaScript
- [Tagged Template Literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates) - JavaScript's equivalent feature

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting PRs.

### How to Contribute

1. Check for existing entries before adding new ones
2. Test all code examples with Python 3.14+
3. Verify all links are working
4. Follow the established format
5. Add meaningful descriptions

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This work is licensed under a [Creative Commons Zero v1.0 Universal License](LICENSE).
