# Tisa-lab3-variant1

This repo is the Lab3 of Computational Process Organization in ITMO, 2022 spring.

**Mathematical expression by expression tree**

- Input language is a sting like a + 2 * sin(*0.3)*(b * c).
- Should support user
- specific functions by passing something like {"foo": lambda x:x*42 } or named arguments.
- Run*time error should be processed correctly.
- You should use the default Python logging module to make the interpreter work trans*parent.
- Visualization as a dataflow graph (see Fig. 5.3) and as a dataflow graph with trace.

## Project structure description

* `MathExpTree.py` -- includes class `MathExpTree` with functions`convert` and `visualize`,`evaluate`

* `MathExpTree_test.py` -- unit  tests for `MathExpTree.py`.

## Contribution

* Chen Biao(1377681089@qq.com)
  * Implement the `MathExpTree.py`
  * Write `README.md`
  * Source code framework construction

* Guo Zhaoxin(zhaoxin_guo@163.com)
  * Implement the `MathExpTree_test.py`
  * Write `README.md`
  * Created GitHub repository

## Features

* `convert()`: Converts the original formula to a postfix expression.
* `visualize`: visualize dataflow. 
* `evaluate`: Evaluate result of the expression.

## Changelog

* 20.5.2022 - 2
  * update `README.md`
* 14.5.2022 - 1
  * update `MathExpTree.py` and `MathExpTree_test.py`
* 11.5.2022 - 0
  * Initial.

## Design notes

* Parse input string in a tree
