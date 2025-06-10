# Contributing to Awesome T-Strings

First off, thank you for considering contributing to Awesome T-Strings! This curated list thrives on community contributions, and we appreciate your help in making it a comprehensive resource for Python's template strings.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Suggesting New Resources](#suggesting-new-resources)
  - [Improving Existing Content](#improving-existing-content)
  - [Reporting Issues](#reporting-issues)
- [Contribution Guidelines](#contribution-guidelines)
  - [Quality Standards](#quality-standards)
  - [Formatting Requirements](#formatting-requirements)
  - [Categories](#categories)
- [Submission Process](#submission-process)
- [Review Process](#review-process)

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## How Can I Contribute?

### Suggesting New Resources

We welcome suggestions for:
- Libraries and tools that use t-strings
- Tutorials and learning materials
- Blog posts and articles
- Conference talks and videos
- Real-world examples and use cases
- IDE plugins and extensions

### Improving Existing Content

You can help by:
- Fixing broken links
- Updating outdated information
- Improving descriptions
- Adding missing context
- Correcting technical inaccuracies

### Reporting Issues

If you find problems, please [open an issue](https://github.com/t-strings/awesome-t-strings/issues) with:
- A clear title and description
- Links to the problematic content
- Suggestions for improvement

## Contribution Guidelines

### Quality Standards

Before submitting a resource, ensure it meets these criteria:

#### For Libraries/Tools
- ✅ **Python 3.14+ compatible** - Must work with template strings
- ✅ **Actively maintained** - Recent commits (within 6 months)
- ✅ **Well documented** - Clear README and usage examples
- ✅ **Properly tested** - Has test suite or examples
- ✅ **Adds value** - Solves a real problem or demonstrates best practices

#### For Articles/Tutorials
- ✅ **Technically accurate** - Information is correct and up-to-date
- ✅ **Well written** - Clear, concise, and easy to understand
- ✅ **Includes examples** - Working code demonstrating concepts
- ✅ **Recent** - Published within the last 2 years (unless historically significant)

#### For Videos/Talks
- ✅ **Good quality** - Clear audio and video
- ✅ **Educational value** - Teaches concepts effectively
- ✅ **Accessible** - Available without paywall

### Formatting Requirements

Follow this format exactly:

```markdown
- [Resource Name](https://example.com) - Brief description ending with a period.
```

#### Examples

✅ **Good:**
```markdown
- [sql-tstring](https://github.com/pgjones/sql-tstring) - Safe SQL query building with t-strings, preventing SQL injection.
- [t-linter](https://github.com/koxudaxi/t-linter) - Comprehensive linting tool for template strings with IDE integrations.
```

❌ **Bad:**
```markdown
- [sql-tstring](https://github.com/pgjones/sql-tstring) - sql library (missing detail, no period)
- sql-tstring - https://github.com/pgjones/sql-tstring (wrong format) 
- [SQL TString](github.com/pgjones/sql-tstring) - Library for SQL. (inconsistent naming, incomplete URL)
- [Tool Name](https://example.com) - A tool for t-strings (vague description)
```

### Categories

Place your contribution in the appropriate section:

1. **Official Resources** - PEPs, Python docs, official tools
2. **Development Tools** - Linters, formatters, IDE extensions
3. **Libraries & Frameworks** - Packages that use or support t-strings
4. **Learning Resources** - Tutorials, courses, documentation
5. **Community** - Discussions, forums, social media

If unsure about categorization, mention it in your PR description.

## Submission Process

1. **Fork the repository**
   - Click the "Fork" button on the [repository page](https://github.com/t-strings/awesome-t-strings)
   - Clone your fork:
   ```bash
   git clone https://github.com/<your-github-username>/awesome-t-strings.git
   cd awesome-t-strings
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b add-amazing-resource
   ```

3. **Make your changes**
   - Add your resource in the appropriate section
   - Maintain alphabetical order within sections
   - Ensure proper formatting

4. **Test your changes**
   - Check all links work (use `python scripts/validate_links.py`)
   - Verify markdown renders correctly
   - Preview your changes locally
   - Ensure no broken formatting

5. **Commit your changes**
   ```bash
   git add README.md
   git commit -m "feat: add amazing-t-string-library for HTML templating"
   ```

   Use these commit prefixes:
   - `feat:` - Adding new resources
   - `fix:` - Fixing links or errors
   - `docs:` - Updating documentation
   - `style:` - Formatting changes

6. **Push to your fork**
   ```bash
   git push origin add-amazing-resource
   ```

7. **Submit a Pull Request**
   - Go to your fork on GitHub
   - Click "New pull request"
   - Use a clear, descriptive title
   - Describe what you're adding and why it's valuable
   - Link to relevant issues if any
   - Review the diff to ensure accuracy

## Review Process

### What to Expect

1. **Automated checks** - Links validation, format checking
2. **Maintainer review** - Usually within 3-5 days
3. **Community feedback** - Others may comment
4. **Revisions** - You may be asked to make changes

### Review Criteria

Maintainers will check:
- ✅ Meets quality standards
- ✅ Properly formatted
- ✅ Adds value to the list
- ✅ No duplicates
- ✅ Appropriate category

### After Acceptance

Once merged:
- Your contribution will be live
- You'll be added to contributors
- The community benefits from your addition!

## Additional Notes

### For Maintainers

If you're interested in becoming a maintainer:
- Contribute regularly
- Help review PRs
- Engage with the community
- Contact current maintainers

### Questions?

If you have questions:
- Check existing issues first
- Join community discussions
- Open a new issue with the "question" label

Thank you for helping make Awesome T-Strings better!