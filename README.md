# How to Debug Python with VSCode

## Summary

- [Basic](#basic)
- [Spec](#spec)
- [Instruction](#instruction)
- [unit test](#unit-test)
- [executable file debug](#executable-file-debug)

## Basic

- [Python.org](https://www.python.org/)
- Extension: [Python](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python)
- Debugger: Python
- module code: [bubble_sort.py](https://github.com/74th/vscode-debug-specs/blob/master/python/bubble_sort.py)

## Spec

- OS
  _ ✅ MacOS
  _ ✅ Windows \* ✅ Linux
- Break Point
  _ ✅ break point
  _ ❓ condition break point : it does not work on my machine, always breaks
  _ ❌ function breakpoint
  _ ✅ uncaught exception breakpoint \* ✅ all exception breakpoint
- Step Execution
  _ ✅ Step Over
  _ ✅ Step Into
  _ ✅ Step Out
  _ ✅ Continue
- Variables
  _ ✅ variables views
  _ ✅ watch variables
- Call Stack \* ✅ call stack
- Evaluation
  _ ✅ eval expression to show variables
  _ ✅ eval expression to change variables
- Type of Execution
  _ ✅ debug unit test
  _ ✅ debug executable package \* ❓ remote debugging

## Instruction

Only installing Extension.

### additional

If you want to pyenv or other environment tools, select your environment with belong way.

`F1`->`Python: Select Workspace Interpreter`

![SelectWorkspaceInterpreter1.png](SelectWorkspaceInterpreter1.png)

![SelectWorkspaceInterpreter2.png](SelectWorkspaceInterpreter2.png)

## unit test

- test code: [test_bubble_sort.py](https://github.com/74th/vscode-debug-specs/blob/master/python/test_bubble_sort.py)

### inline

`F1`->`Python: Run Current Unit Test File`

![CodelensUnitTest1.png](CodelensUnitTest1.png)

`Enable and configure a Test Framework.`->select your test framework.

![CodelensUnitTest2.png](CodelensUnitTest2.png)
![CodelensUnitTest3.png](CodelensUnitTest3.png)

sample: `unittest`->`.`->`test_*`

![CodelensUnitTest4.png](CodelensUnitTest4.png)
![CodelensUnitTest5.png](CodelensUnitTest5.png)

Codelens on test function shows run and debug test button.

![CodelensUnitTest6.png](CodelensUnitTest6.png)

But it sometimes doesn't start debug in my machine. Then, it restarts VSCode and retry.

### use launch.json

Menu: Python:Python module

![DebugPythonModule](DebugPythonModule.png)

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Module",
      "type": "python",
      "request": "launch",
      "stopOnEntry": true,
      "pythonPath": "${config:python.pythonPath}",
      "module": "unittest",
      "args": [
        // test package
        // <test_file>
        // <test_file>.<test_class>
        // <test_file>.<test_class>.<test_method>
        "test_bubble_sort.TestBubbleSort.test_bubble_sort"
      ],
      "cwd": "${workspaceRoot}",
      "env": {},
      "envFile": "${workspaceRoot}/.env",
      "debugOptions": [
        "WaitOnAbnormalExit",
        "WaitOnNormalExit",
        "RedirectOutput"
      ]
    }
  ]
}
```

### debug with integrated terminal

Menu: Python: Python program with Integrated Terminal/Console

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Integrated Terminal/Console",
      "type": "python",
      "request": "launch",
      "stopOnEntry": true,
      "pythonPath": "${config:python.pythonPath}",
      "program": "bubble_sorter.py",
      "cwd": "",
      "console": "integratedTerminal",
      "env": {},
      "envFile": "${workspaceRoot}/.env",
      "debugOptions": ["WaitOnAbnormalExit", "WaitOnNormalExit"]
    }
  ]
}
```

## executable file debug

executable file: [bubble_sorter.py](https://github.com/74th/vscode-debug-specs/blob/master/python/bubble_sorter.py)

note: ![DebugPython](DebugPython.png)

### launch.json

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python",
      "type": "python",
      "request": "launch",
      "stopOnEntry": true,
      "pythonPath": "${config:python.pythonPath}",
      //"program": "${file}",
      "program": "bubble_sorter.py",
      "args": ["4", "3", "2", "1"],
      "cwd": "${workspaceRoot}",
      "env": {},
      "envFile": "${workspaceRoot}/.env",
      "debugOptions": [
        "WaitOnAbnormalExit",
        "WaitOnNormalExit",
        "RedirectOutput"
      ]
    }
  ]
}
```

## remote debug

TODO: This do not work on my machine!

### prepare

install pyvsd package

```sh
pip install ptvsd
```

### code

add remote debug code.

```python
import ptvsd

ptvsd.enable_attach("nnyn", address=('0.0.0.0', 3333))
ptvsd.wait_for_attach()
```

run follow command.

```sh
python bubble_sorter_for_remote.py 4 3 2 1
```

### launch.json

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach (Remote Debug)",
      "type": "python",
      "request": "attach",
      "localRoot": "${workspaceRoot}",
      "remoteRoot": "${workspaceRoot}",
      "port": 3000,
      "secret": "my_secret",
      "host": "localhost"
    }
  ]
}
```
