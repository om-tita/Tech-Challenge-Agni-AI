# Coding Conventions for eCommerce Site for Pets

## General Guidelines
- Follow consistent naming conventions for files and directories.
- Use camelCase for JavaScript variables and functions.
- Use PascalCase for React components.
- Use kebab-case for CSS class names.

## JavaScript
- Use ES6+ syntax (e.g., arrow functions, destructuring).
- Use `const` and `let` instead of `var`.
- Keep functions small and focused on a single task.
- Use meaningful variable and function names.
- Comment complex logic and important decisions.

## React
- Organize components in a logical folder structure.
- Use functional components and hooks where possible.
- Keep component state minimal and derived from props when possible.
- Use PropTypes for type checking of component props.
- Ensure components are reusable and maintainable.

## CSS
- Use a preprocessor like SASS or LESS for styles.
- Organize styles in a modular way, ideally co-locating styles with components.
- Use BEM (Block Element Modifier) methodology for class naming.
- Avoid inline styles; prefer CSS classes.

## Git
- Use meaningful commit messages (e.g., `Add product listing component`).
- Commit often with small changes rather than large, monolithic commits.
- Use branches for features, fixes, and experiments.

## Documentation
- Document all public functions and components.
- Maintain an updated README.md with setup instructions and project overview.
- Use JSDoc for documenting JavaScript code.

## Testing
- Write unit tests for all components and utility functions.
- Use Jest and React Testing Library for testing React components.
- Ensure tests are easy to read and maintain.

## Code Reviews
- Conduct code reviews for all pull requests.
- Provide constructive feedback and suggestions for improvement.
- Ensure adherence to coding conventions during reviews.