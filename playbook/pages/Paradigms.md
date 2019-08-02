# Paradigms

## TDD

- Write a test - test fleshes out some functionality in the app
- Run the test - it should fail as we have no code yet to make it run
- Write the code - enough to make the test pass
- Run the test - if it passes, our code meets the test requirement
- Refactor - Remove duplication, optimise, or make it readable then re-run the tests
- Repeat - profit.

## Staticmethod

If it doesn't need access to the class or the instance...but is thematically related to the class (typical example: helper functions and conversion functions used by other class methods or used by alternate constructors), then use staticmethod

## [OOP](OOP)

### Composition over Inheritance
