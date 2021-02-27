---
title: Flakehell configuration file
---

## Context

To run [flakehell] with a custom config, I tried the following commands:

```shell
flakehell lint --config https://raw.githubusercontent.com/Recall-Masters/standards/main/pyproject.toml jeeves
flakehell lint --config ~/projects/builder/pyproject.toml jeeves
```

neither of which worked. It seems flakehell just ignores the `--config` option.

## Decision

We will have to rely upon the standard `pyproject.toml`. Thanks to the [`base`](https://flakehell.readthedocs.io/config.html#base) option, we will be able to reuse remote configs. Will rely on that for now.

## Consequences

The user will have to configure the `[tool.flakehell]` section themselves. This is not ideal, but I think we can live with this for now. Users will have that section in place by default if they use [yeti-python-package](https://github.com/anatoly-scherbakov/yeti-python-package) which I intend to merge with `mister-jeeves` project.
