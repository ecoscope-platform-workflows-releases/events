# events
A dashboard for visualizing events.

## Recompiling

To recompile this workflow after having made changes to `spec.yaml`, first install `wt-compiler`
if you do not have it installed already:

> NOTE: The `--run-post-link-scripts` flag is necessary because, in order to generate a visual
representation of the workflow DAG, the `wt-compiler compile` command depends on the `dot` executable
having been initialized post-install via the `dot -c` command. Setting the `--run-post-link-scripts`
flag triggers this initialization automatically. Setting this flag does imply allowing the package
manager to [run (potentially insecure) arbitrary scripts](https://pixi.prefix.dev/v0.62.2/reference/pixi_configuration/#run-post-link-scripts).
If you prefer to omit this flag, then after you have installed `wt-compiler`, you may
separately run `$HOME/.pixi/envs/wt-compiler/bin/dot -c` to initialize `dot`.

```console
$ pixi global install \
-c https://prefix.dev/ecoscope-workflows \
-c conda-forge \
wt-compiler \
--run-post-link-scripts
```

Then from the repo root, run:

```console
$ wt-compiler compile \
--spec=spec.yaml \
--pkg-name-prefix=ecoscope-workflows \
--results-env-var=ECOSCOPE_WORKFLOWS_RESULTS \
--variant=gcp \
--update \
--clobber

```
