# simplegoal
`simplegoal` is the new and simple way to manage your long term (or short term) goals.


## Quickstart
Typically, `simplegoal` prompts you to define goal in **two steps** as following:

1. Define the **master goal** (long term process).
```shell
simplegoal add [goal] [modifiers]
```

2. Define *how you would like to achive your goal* (steps).
```shell
simplegoal steps --master [goal] add [step] [modifiers] 
```

More on *modifiers* below.

**To see the list of goals:**
```shell
simplegoal
```

**To see the list of steps in a goal:**
```shell
simplegoal steps --master [goal]
```two steps

**Delete a goal will delete its steps:**
```shell
simplegoal delete [goal_id]
```

**Delete a step in a goal:**
```shell
simplegoal steps --master [goal] delete [step_id]
```

## Modifiers
### Goal modifiers
- `--time-target [duration]`: for goals with duration as their target.
- `--freq-target [count]`: for goals with frequency as their target.
- `--end [due]`: specify when this goal will end.

As an example, this commandline:
```shell
simplegoal add Learn algorithms --time-target 210h --end eoy
```
is equivalent to saying: *"My goal is to dedicate 210 hours for learning algorithms by the end of the year (eoy)"*

Another example,
```shell
simplegoal add Reading books --freq-target 20 --end 16-02-2022
```

is equivalent to saying: *"I will finish 20 books/chapters/paragraphs by 16/02/2022"*

### Step modifiers
- `--every [frequency]`: for steps with recurrence. For example `--every 2d` means recurs every 2 days.

`simplegoal` has actually defined some convenient modifiers such as `--daily`, `--weekly`, `--monthly`, `--yearly`

Example:
```shell
simplegoal steps --master 1 add Watch youtube tutorials --every 7d
```

is equivalent to saying: *"To achive my goal, I will watch Youtube tutorials every week (7 days)"* `simplegoal` will then automatically distribute the amount of time per week that you have to spend on watching Youtube tutorials.
