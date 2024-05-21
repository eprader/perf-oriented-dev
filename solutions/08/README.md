# A) False Sharing

# B) Data Structure Selection

The pull request I found is maurycyw/StaggeredGridView#63 

[link](https://github.com/maurycyw/StaggeredGridView/pull/63)

In this pull request The mapping of grid positions is moved from an `ArrayList` to a `HashSet`.

The data structure in question seems to store the positions of elements that should be displayed in a grid.
Every element should vary in the size it has on the screen. An element can span multiple columns e.g has multiple positions it is at.
The View checks if the element is currently in view (the position is contained in the position set of the element).

Operations like `contains()` and `remove()` are invoked many times for the elements in this data structure.
Using a `HashSet` instead of an `ArrayList` reduces the complexity of these operations from `O(n)` to `O(1)`.

Memory layout is actually negatively impacted by this change because of random memory access due to
use of a hash function. In addition, memory usage might be higher if the `HashSet` is not populated completely.

* Type of data stored: Position in a grid
* Access patterns:
  * Populating grid with elements of different sizes
  * check position in grid via `contains()`
  * `remove` elements
* Hardware properties were not relevant in this case.
