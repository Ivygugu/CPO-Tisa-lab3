# Tisa- lab3 - variant1

This repo is the Lab3 of Computational Process Organization in ITMO, 2022 spring.

## Project structure description

- `expression_tree.py` -- includes class `Node` with methods `__init__` and `get_priority`,
 class `ExpressTree` with methods `__init__`, `__preprocess`, `__build_express_tree`,
 `__update_value`, `__call__`, `visualization`,
 and function `arg_type` as a decorator for checking input datas.

- `expression_tree_test.py` -- unit tests for `expression_tree.py`.

## Contribution

- Chen Biao(1377681089@qq.com)
  - Implement the `expression_tree.py`
  - Write `README.md`
  - Source code framework construction

- Guo Zhaoxin(zhaoxin_guo@163.com)
  - Implement the `expression_tree_test.py`
  - Write `README.md`
  - Created GitHub repository

## Features

- class `Node`:
  - `__init__`: Instantiate a node of expression tree
 (non-leaf - function; leaf - constant).
  - `get_priority`: Get the priority of function.

- class `ExpressTree`:
  - `__init__`: Create an expression tree.
  - `__preprocess`: Preprocessing the input string expression.
  - `__build_express_tree`: Building an expression tree
   according to the preprocessed string expression.
  - `__update_value`: Reducing the expression tree in a result (from leaves to root).
  - `__call__`: Input constants, reduce the expression.
  - `visualization`: Visualization the expression tree.

## Changelog

- 01.6.2022 -2
  - update `README.md`
- 20.5.2022 -1
  - update `expression_tree.py` and `expression_tree_test.py`
- 18.5.2022 -0
  - Initial.

## Design notes

- Input type: string.
- In expression tree, functions are parsed as non-leaf nodes and constants as leave.
- Users can customize functions as non-leaf nodes of the expression tree.
