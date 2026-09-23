# Python Fundamentals — Cheat Sheet

Quick definitions from session `00_python_fundamentals`. Keep this open while you practise.

---

## Showing output


| Term         | Meaning                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------- |
| `print(...)` | Displays a value on the screen (under a notebook cell, or in the terminal for a script). |


---

## Variables and types


| Term             | Meaning                                                           |
| ---------------- | ----------------------------------------------------------------- |
| **Variable**     | A **name** that refers to a **value** (e.g. `currency = "USDT"`). |
| **Assign (`=`)** | Store a value under a name. Not the same as “equals” in maths.    |
| **Types**        | Give the same name a new value later (`currency = "BTC"`).        |
| `str`            | Text (a **str**ing), e.g. `"USDT"`.                               |
| `int`            | A whole number (**int**eger), e.g. `3`.                           |
| `float`          | A number with a decimal, e.g. `1.5`.                              |
| `bool`           | `True` or `False` (**bool**ean).                                  |
| `type(x)`        | Tells you what kind of value `x` is.                              |


**Quotes rule:** `"currency"` is the text spelling currency. `currency` (no quotes) means the variable’s value.

---

## Strings and numbers


| Term              | Meaning                                                 |
| ----------------- | ------------------------------------------------------- |
| **Index**         | Position of a character/item. Counting starts at **0**. |
| `s[0]`            | First character of string `s`.                          |
| `s[:8]`           | First 8 characters (a short preview).                   |
| `len(s)`          | How long `s` is.                                        |
| `float("349999")` | Turn text that looks like a number into a real number.  |
| `str(1.5)`        | Turn a number into text.                                |



---

## Arithmetic

| Operator | Meaning |
|----------|---------|
| `+` `-` `*` `/` | Add, subtract, multiply, divide |
| `//` | Divide, keep whole number only |
| `%` | Remainder after division |
| `**` | Power (e.g. `2 ** 3` is `8`) |
| `total += x` | Same as `total = total + x` |

Use `( )` for order: `(10 + 5) * 2` vs `10 + 5 * 2`.

---

## Collections


| Term                    | Meaning                                                           |
| ----------------------- | ----------------------------------------------------------------- |
| **List** `[...]`        | Ordered collection. Can have duplicates.                          |
| `list[0]`               | First item in the list.                                           |
| `len(list)`             | How many items.                                                   |
| `list.append(x)`        | Add `x` to the end.                                               |
| **Dictionary** `{...}`  | Labels (**keys**) mapped to **values**, e.g. `{"amount": 1000}`.  |
| `d["key"]`              | Look up a value (errors if the key is missing).                   |
| `d.get("key", default)` | Look up a value safely; returns `default` if missing.             |
| **Set**                 | Collection of **unique** values (no duplicates; order not fixed). |
| `set(my_list)`          | Turn a list into a set (drops duplicates).                        |
| `list(my_set)`          | Turn a set back into a list.                                      |


---

## Operators and booleans


| Operator  | Meaning                           |
| --------- | --------------------------------- |
| `==`      | Equal to (compare).               |
| `!=`      | Not equal to.                     |
| `>` `<`   | Greater than / less than.         |
| `>=` `<=` | Greater/less than or equal.       |
| `and`     | Both sides must be `True`.        |
| `or`      | At least one side must be `True`. |
| `not`     | Flip `True` ↔ `False`.            |


A comparison like `amount > 5000` **resolves to** a boolean (`True` or `False`).

Combined conditions resolve in steps, e.g.
`(10 > 5) and (9 == 9)` → `True and True` → `True`.
With `and`, every part must be `True`. With `or`, one `True` is enough.

---

## Conditionals and loops


| Term              | Meaning                                                          |
| ----------------- | ---------------------------------------------------------------- |
| `if`              | Run indented code only when the condition is `True`.             |
| `elif`            | “Else if” — try another condition.                               |
| `else`            | Run if none of the conditions above were `True`.                 |
| **Indentation**   | Leading spaces that show which lines belong to an `if` or `for`. |
| `for x in items:` | Repeat the indented block once for each item in `items`.         |


`if transfer["type"] == "deposit":` means: run the block when that comparison is `True` (same idea as storing it in a variable first).

---

## Functions


| Term             | Meaning                                         |
| ---------------- | ----------------------------------------------- |
| `def name(...):` | Define a reusable recipe (a **function**).      |
| **Call**         | Run the function, e.g. `usd_value(2.0, 70000)`. |
| `return`         | Send a result back from the function.           |


---

## Notebooks vs scripts


| Term                    | Meaning                                               |
| ----------------------- | ----------------------------------------------------- |
| **Notebook** (`.ipynb`) | Interactive document; run code cell by cell.          |
| **Script** (`.py`)      | Plain Python file; run with `python path/to/file.py`. |


---

## Common errors


| Error        | Typical cause                                  |
| ------------ | ---------------------------------------------- |
| `NameError`  | Using a name you never defined (often a typo). |
| `TypeError`  | Wrong type for an operation (e.g. `"1" + 2`).  |
| `KeyError`   | Dictionary key does not exist.                 |
| `IndexError` | List index out of range.                       |


Read the **last line** of the error message first.