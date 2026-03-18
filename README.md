# events
A dashboard for visualizing events.

## Recompiling

To recompile this workflow after having made changes to `spec.yaml`, run:

> TODO: `wt-compiler` install instructions

```console
$ wt-compiler compile \
--spec=spec.yaml \
--pkg-name-prefix=ecoscope-workflows \
--results-env-var=ECOSCOPE_WORKFLOWS_RESULTS \
--variant=gcp \
--update \
--clobber

```
