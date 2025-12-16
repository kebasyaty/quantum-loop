#
#  .::::::.    ...    :::  :::.   :::.    :::.::::::::::::...    :::.        :
# ,;;'```';;,  ;;     ;;;  ;;`;;  `;;;;,  `;;;;;;;;;;;'''';;     ;;;;;,.    ;;;
# [[[     [[[\[['     [[[ ,[[ '[[,  [[[[[. '[[     [[    [['     [[[[[[[, ,[[[[,
# "$$c  cc$$$"$$      $$$c$$$cc$$$c $$$ "Y$c$$     $$    $$      $$$$$$$$$$$"$$$
#  "*8bo,Y88b,88    .d888 888   888,888    Y88     88,   88    .d888888 Y88" 888o
#    "*YP" "M" "YmmMMMM"" YMM   ""` MMM     YM     MMM    "YmmMMMM""MMM  M'  "MMM
#  :::         ...         ...   ::::::::::.
#  ;;;      .;;;;;;;.   .;;;;;;;. `;;;```.;;;
#  [[[     ,[[     \[[,,[[     \[[,`]]nnn]]'
#  $$'     $$$,     $$$$$$,     $$$ $$$""
# o88oo,.__"888,_ _,88P"888,_ _,88P 888o
# """"YUMMM  "YMMMMMP"   "YMMMMMP"  YMMMb
#
#
# Copyright (c) 2025 Gennady Kostyunin
# Quantum Loop is free software under terms of the MIT License.
# Repository https://github.com/kebasyaty/quantum-loop
#
"""A set of tools for quantum calculations.

A Qubit in a regular computer is quantum of algorithm that is executed in
one iteration of a cycle in a separate processor thread.

Quantum is a function with an algorithm of task for data processing.

In this case, the Qubit is not a single information,
but it is a concept of the principle of operation of quantum calculations on a regular computer.
"""

from __future__ import annotations

__all__ = (
    "QuantumLoop",
    "LoopMode",
    "count_qubits",
)


from ql.loop import QuantumLoop
from ql.utils import LoopMode, count_qubits
