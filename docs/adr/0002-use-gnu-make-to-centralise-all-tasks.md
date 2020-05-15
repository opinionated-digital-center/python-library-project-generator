# Use GNU Make to centralise all tasks

* Status: accepted
* Date: 2020-05-07

## Context and Problem Statement

We want to be able to centralise in a single tool all tasks to be called:
* During the development cycle.
* During the build cycle.
* In the CI/CD pipelines.

## Decision Drivers

* Must have a significant user base and community.
* Must not require significant installation.
* Must be sufficiently simple to learn and use.

## Considered Options

* [`GNU Make`](https://www.gnu.org/software/make/).
* [`Invoke`](http://www.pyinvoke.org/).
* [`Rake`](https://github.com/ruby/rake).
* [`SCons`](https://scons.org/).

## Decision Outcome

Chosen option: `GNU Make`, because compared to the other evaluated tools (see
[Pros and Cons](#pros-and-cons-of-the-options)), it fits the bill where as:
* `Invoke` is not well maintained, nor well documented, nor a de facto standard, nor has
  a sufficient community.
* `Rake` required to install and learn Ruby.
* `SCons` is more a build tool and seems difficult to apprehend/get to grips with.

## Pros and Cons of the Options

### [`GNU Make`](https://www.gnu.org/software/make/)

`GNU Make` [manual](https://www.gnu.org/software/make/manual/).

* Good, because:
  * It is a well known and widely used standard.
  * It has a huge existing community.
  * It is pre-installed by default on most systems, and can easily be installed on
    most existing systems.
  * It does not require to install a specific language (python, ruby, etc.)
  * It does enough for the purpose of writing and using tasks.
  * It has plenty of documentation.
  * It has plenty of existing information sources.
* Bad, because:
  * Some concepts can be difficult to grasp for our use.
  * Some default behaviors can be unclear and cause scripts not to work.
  * It can be difficult to debug when using complex features.

### [`Invoke`](http://www.pyinvoke.org/)

* Good, because:
  * It is Python based.
  * It promises:
    * Like Ruby’s Rake, a clean, high level API.
    * Like GNU Make, an emphasis on minimal boilerplate for common patterns
      and the ability to run multiple tasks in a single invocation.
* Bad, because:
  * It is not a de facto standard for Python.
  * It has a large number of
    [unresolved and untriaged issues](https://github.com/pyinvoke/invoke/issues)
    (202 at time of writing) and a large number of
    [opened Pull Requests](https://github.com/pyinvoke/invoke/pulls), some dating back
    2014, which suggests a slack in maintenance.
  * It does not seem to have a large enough community.
  * Previous points seem to disqualify this solution.

### [`Rake`](https://github.com/ruby/rake)

* Good, because:
  * It is a proven tool.
  * It is a de facto standard in the Ruby world.
  * It has an extensive community.
  * It has extensive documentation.
* Bad, because:
  * It requires to know/learn another language than Python (Ruby).
  * It requires to install a Ruby stack.

### [`SCons`](https://scons.org/)

* Good, because:
  * Written in Python.
  * Seems fairly active.
* Bad, because:
  * A build tool more than a task tool.
  * Getting to grip the tool through the documentation is cumbersome.
  * It has a large number of
    [unresolved and untriaged issues](https://github.com/pyinvoke/invoke/issues)
    (604 at time of writing), which suggests a slack in maintenance.
  * Limited number of stars on github.
