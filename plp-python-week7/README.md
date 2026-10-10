# Python Week 7 Assignment - Shopping List Manager & List Operations

* `list_warmup.py`: Demonstrates fundamental list operations including index referencing, element appending/removal, and length calculation.
* `shopping_list.py`: Implements an interactive command-line shopping list manager supporting item additions, safe deletions, list viewing, and program termination.
* `list_report.py`: Processes a collection of items to generate numbered lists, count character lengths, and identify the longest string entry.

## Reflection
It is safer to check membership with `in` before calling `.remove()` because attempting to remove an item that does not exist in a list triggers a `ValueError` and causes the program to crash. Checking beforehand allows the program to handle missing elements gracefully and display a friendly user notice instead.