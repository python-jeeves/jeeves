---
title: Custom Commands
position: 2
---

## Context

We need a way to create custom top-level commands, say `jeeves tf`. I can see two methods to do that:

1. Create a new class `JeevesTerraform(Injector)` which then will be added to other classes using the `&` operator;
2. Create a new class `JeevesTerraform(Injector)` which will be dynamically embedded into the main `Jeeves` class as `tf = JeevesTerraform`. Where to get the name `tf` from, then?

## Decision

I am positive that the commands should be represented as tree of `Injector` classes because that allows to interact between them. I believe that the second variant provided above should be chosen because it allows to very flexibly alter the injectors tree.
