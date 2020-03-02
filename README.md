# Locust Runner

[![Travis](https://img.shields.io/travis/hanpeter/locust-runner.svg?logo=travis)](https://travis-ci.org/hanpeter/locust-runner)
[![GitHub tag](https://img.shields.io/github/tag/hanpeter/locust-runner.svg?logo=github)](https://github.com/hanpeter/locust-runner/tags)
[![GitHub last commit](https://img.shields.io/github/last-commit/hanpeter/locust-runner.svg?logo=github)](https://github.com/hanpeter/locust-runner/commits)
[![Requires.io](https://img.shields.io/requires/github/hanpeter/locust-runner.svg)](https://requires.io/github/hanpeter/locust-runner/requirements)
[![license](https://img.shields.io/github/license/hanpeter/locust-runner.svg)](LICENSE)

`locust-runner` is a helper for [`locust`](https://locust.io/) to allow users to build Locust tests using a YAML file.

Example test command:
```bash
$ locust -f locust_runner/runner.py --no-web -c 1 -r 1 -t 10s --only-summary
```
