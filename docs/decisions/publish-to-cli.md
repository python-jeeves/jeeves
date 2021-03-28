---
title: Publish a command to CLI
position: 3
---

## Suggestion

In an `Injector` member function, return a `Callable` that will accept CLI arguments and whatnot.

## Declined

Because that will mean we will have to execute every member of every `Injector` on instantiation.
