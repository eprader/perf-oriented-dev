# A) False Sharing

# B) Data Structure Selection

The pull request I found is maurycyw/StaggeredGridView#63 

[link](https://github.com/maurycyw/StaggeredGridView/pull/63)

In this pull request The mapping of grid positions is moved from an `ArrayList` to a `HashSet`.

The data structure in question seems to store the Positions of elements that should be displayed in a grid.

Operations like `contains()` and `remove()` are invoked many times for the elements in this data structure.
Using a `HashSet` instead of an `ArrayList` reduces the complexity of these operations from `O(n)` to `O(1)`.

Memory layout is actually negatively impacted by this change because of random memory access due to
use of a hash function. In addition, memory usage might be higher if the `HashSet` is not populated completely.

* Type of data stored: Position in a grid
* Access patterns:
  * populated initially
  * check position in grid via `contains()`
  * `remove` elements
