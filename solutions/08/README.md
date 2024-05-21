# A) False Sharing
When different threads modify data from the same cache line at the same time, this leads to cache invalidation which might lead to performance issues.

The PR KhronosGroup/Vulkan-ValidationLayers#5587 solves such an issue.

In the above PR mutex locks are padded to be on separate cache lines so that concurrent access to these locks does not lead to false sharing.
The PR replaces the original manual padding with a method call of `alignas` with a custom constant expression `get_hardware_destructive_interference_size()`
which evaluates to `64`. The intent is to use existing means for padding instead of a handcrafted solution.

Originally the PR mentions the constant `std::hardware_destructive_interference_size` which would provide a uniform interface to read the 
`L1` cache line size from the system. 
See [official documentation of c++17](https://en.cppreference.com/w/cpp/thread/hardware_destructive_interference_size#Notes)

The PR falls back to a custom method with only the hard-coded cache line size of `64` because the check,
if the use of `std::hardware_destructive_interference_size` is supported is only
available in `c++20`. A `TODO` was added to fix this in the future.

Main problems with the constant were on Linux / Android according to the comments of the PR

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

Having evaluation criteria such as those discussed in the lecture helps with evaluating and comparing of potential data structures.
Depending on the use case, some of the discussed criteria are not applicable. (e.g. hardware independent software)
