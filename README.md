# Tisa- lab3 - variant1

This repo is the Lab3 of Computational Process Organization in ITMO, 2022 spring.

## Project structure description

- `MathExpTree.py` -- includes class `MathExpTree` with functions`convert` and `visualize`,`evaluate`

- `MathExpTree_test.py` -- unit  tests for `MathExpTree.py`.

## Contribution

- Chen Biao(1377681089@qq.com)
  - Implement the `MathExpTree.py`
  - Write `README.md`
  - Source code framework construction

- Guo Zhaoxin(zhaoxin_guo@163.com)
  - Implement the `MathExpTree_test.py`
  - Write `README.md`
  - Created GitHub repository

## Features

- `convert()`: Converts the original formula to a postfix expression.

- `visualize`: visualize dataflow. 

- `evaluate`: Evaluate result of the expression.

## Changelog

- 01.6.2022 -2
  - update `README.md`
- 20.5.2022 -1
  - update `MathExpTree.py` and `MathExpTree_test.py`
- 18.5.2022 -0
  - Initial.

## Design notes

### Compare mutable and immutable implementation

- Mutable Infrastructure

  - Fix problems more quickly.
  - The infrastructure can more precisely fit the specific needs.
  - Updates are usually faster and can be adapted to each individual server.

- Immutable Infrastructure

  - Discrete versioning means tracking and rollbacks are much easier.
  - Testing is easier to run.
  - Predictable state since the infrastructure is never modified, reducing complexity.
  - Safe thread code in a multi-threaded environment meaning mutation is nonexistent.
  - Supports DevOps and cloud computing.
  - Eliminates configuration drift.
