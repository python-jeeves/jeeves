---
title: Commands must be classes
position: 4
---

## Context

As it is explained at [dependencies/Usage](https://proofit404.github.io/dependencies/usage/), Python functions embedded into Injectors are not used as dependency resolution targets.

That means the user may write `def install(terraform_version)` but `terraform_version` will NOT be resolved. Moreover, the function will not receive any context about the command execution nor any help from other Jeeves injected components.

## Decision

Always use dataclasses (or, say, attrs or Pydantic models) as commands. Due to dependency injection, the system will automatically provide the arguments of these classes. These values will be:

- instances of other classes,
- scalar constant hardcoded values,
- including, say, functions.

During the process of Dependency Injection, nothing but class constructors gets executed.

Class constructors do not contain any business logic.

That means we **can resolve dependencies** when creating the Typer application instead of doing that from Typer specific code.
