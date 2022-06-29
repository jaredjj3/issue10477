# issue10447

Reproduction repo for [#10447](https://github.com/SeleniumHQ/selenium/issues/10447).

## How to run

1. Run the containers.

```bash
docker-compose build && docker-compose run --rm test bash ; docker-compose down
```

2. Wait until you can visit http://localhost:4444.

3. Run `run` in the shell.

## Caveats

This is not supported on M1 macs. See [#9733](https://github.com/SeleniumHQ/selenium/issues/9733).
