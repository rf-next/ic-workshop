# IC workshop 2017-02-25

## The idea

Below I set out a proposed order of activities to do, in order to get
used to the most common Git and Github operations you will need to
perform while working on `IC`.

Please talk to me for clarification of what each item means.

These are just proposals for things that should be useful to do, but,
at any stage, we can talk about any aspect of IC development. The
point of the day is to be as useful to *you* as possible.

Please do *everything* in pairs.

Most of the steps should be repeated many times, as many as it takes
for you to start feeling comfortable with them. We can always come
back to any of them later, so that you can get more practice or
clarification.

At this point, we are doing absolutely no programming whatsoever,
merely getting used to working with Magit and Github, and trying to
understand the IC workflow. So just create and modify files containing
any text you like. The content of the files does not matter at this
point: we want to perform lots and lots of Git operations over and
over again, without getting distracted by any specific programming
domain.

Do not work in the same pair all day long: the pairs should be split
up and mixed every now and then. Seeing different people's
perspectives and styles is an interesting exercise in itself.

## Preliminaries

+ Make sure you have a *graphical* emacs installed. On OS X
   [Emacs for Max OS X](https://emacsformacosx.com/) is a good option.

+ Make sure that you have magit and helm installed. The simplest way
  is to use the
  [init file](https://github.com/nextic/IC/raw/master/doc/init.el)
  provided by IC, by placing it in `~.emacs.d`. This will
  automatically download and configure magit and helm on first use.

## Git, Magit, and Github exercises

+ Upload your ssh keys to Github

+ `git clone git@github.com:jacg/ic-workshop.git`

+ stage & commit a few times on the `master` branch

+ create new branch, few commits, merge

+ few commits, rebase

+ observe what happens to the log when you merge as opposed to rebasing

+ repeat playing with branches, merging vs rebasing

+ In `IC` you can do whatever you want on branches in your local repo
  or your fork, but in the central nextic repo we do not want to see
  any merge commits, unless there is some particularly compelling
  reason for one.

  By default **there are no merge commits** in nextic central repo!

  This means that *someone* will have to rewrite your history *before*
  your work is admitted into the central repo.

+ selective stage

+ commit extend, reword, amend

+ `r i` swap

+ `r i` squash

+ push

+ push -f

+ JG push to central

+ fetch, rebase (reset `b x` (move branch pointer))

+ pull request

+ repeat until understood

+ partial staging

+ reset `X` (soft, hard, mixed, etc.)

+ stash

### Discussion

After doing these exercises, we should have an open discussion to
consider the following questions

+ What are the git operations you will use most?
+ What does the `IC` workflow look like?
+ How do we use branches?
+ What is a pull request?
+ How do you Collaborate with others *before* a pull request?

## Testing with `pytest`

+ I you have not done so already, install spyder: `conda install
  spyder`.

+ pip install
  - hypothesis-numpy
  - flaky
  - pytest-xdist

+ Set up travis for your repo. Ensure that you test on
  [more than one version of Python](https://docs.travis-ci.com/user/languages/python/),
  including at least one version of Python 2 and one version of
  Python 3.

+ Push your changes to your fork every now and then, and observe
  Travis in action.

+ For each of the following Python features

  + Understand and document it, by writing tests.
  + Implement it.

It would probably be interesting to split pairs in the middle each of
these, to see how diffrently others might perceive the same task!

But, before we do any of that, first ...

### Mystery exercise

Let's play a game.

+ The game has two players (or teams): the testers and the
  implementors.

+ The testers write tests

+ The implementors try to pass them ...

+ ... by engaging the the standard TDD practice: do the *simplest*
  thing that will pass the test.

+ But with a twist: the implementors should *maliciously* try to write
  a buggy implementation that passes all the given tests.

+ But let's start by keeping the meaning of the feature secret: the
  implementors will not know the higher-level meaning of what they are
  meant to implement. The *only* communication between the testers and
  the implementors will be the tests.


### `functools.partial`

### `enumerate`

+ Make sure that it works both in Python 2 and 3

+ Implement it in 3 ways

   1. as a class
   2. using generator functions
   3. using 'itertools'

For the second one, it would be best if you start in pairs where at
least one of you is familiar with generator functions (`yield`).

+ Submit each one as a separate commit in your repository.

+ Extract all three implementations from history into the same
  module.

+ Parametrize the tests to test all 3.

+ Now replace the parametrization with a parametrized fixture.

### `collections.namedtuple`

### Pytest features to observe

+ `-k`
+ `-v`
+ `--pdb`
+ `--tb`
+ `-m` and marks
+ `--maxfail`
+ `-s`

## IC exercises

Here are some exercises we can try in the actual IC codebase. Feel
free to propose your own.

Everyone should do the cosmetics exercise, the rest are up to you.

### Cosmetics

This exercise should run continuously, in parallel with any other IC
exercises you are doing. The idea is to simulate lots of need for
pushing, pulling and rebasing, and to demonstrate collaborative
development on a side branch.

At the end of the day, we will squash and merge all cosmetic changes
into master.

+ Make small cosmetic changes to some IC code, on a branch called
  `cosmetics`.

+ Push them to your fork of nextic.

+ Add remotes for at least two other people's forks.

+ Keep doing this repeatedly in small chunks: hopefully you'll get to
  interact with the work of others on the same branch.

### config.py and argparse

This is a very straightforward exercise which should show you the
value of having a good set of tests while refactoring, and get you
into the habit of pressing the test button.

At the moment IC's `core/config.py:configure` function returns a
dictionary containing the configuration settings. This information
would be more conveniently accessible from an `arparse.Namespace`
object (the type that `argparse` uses to store the parsed command line
information); compare

    CFP['OPTION']
    CFP.OPTION

Change the code in IC from the former to the latter style. This
requires two changes:

1. Make `configure` return an `argparse.Namespace` rather than a
   `dict`.

2. Change the lookup of configuration options from the dict style to
   the namespace style, wherever it is necssary in the whole of the IC
   codebase.

How will you know that you have changed it correctly everywhere?

Remove any redundant functions you find in the module.

### City run functions

+ Turn `IRENE`, `ISIDORA`, `MAURILIA` etc. into classmethods with the
  same name. Inherit as much common functionality as possible.

+ Refactor the test fixtures that use these methods.
