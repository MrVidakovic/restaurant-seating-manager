# Design decissions, algorithms and data structures

## Introduction

The challenge here is what data structures to choose because it will influence the available algorithms to use. The problem will require a lot of searching, so an array of `Table` would be convenient as we can load it ordered in the `SeatingManager` class, but any time a table is assigned and unassigned a reordering process would be performed requiring a lot of time. In the other side a double linked list of `Table` would be much quicker for assining and unassigning operations, but searching would be slowed and and it's a critical operation.

So I tryied to design a solution trying to keep both operations as quick as possible. To achieve this I designed the following solution:
- `SeatingManager` will contain a vector with double linked lists of `Table`.
- Each `Table` will have an unique identifier referring the table number in the restaurant as well as the total number of seats.
- Each `Table` will be inserted in the list which index indicates the number of free sits remaining in the table. For example, an empty table with 4 sits will be inserted in the list of index 4 in the vector.
- Insertions in each `Table` list should be ordered based on the table's total number of seats.
- Each `Group` will also have an unique ID. 
- When a `Group` is assigned to a table the table should be moved to the list indicating the remaining number of free sits.
- When a `Group` leaves, it's `Table`  should be searched accross the whole structure. This operation in the most expensive regarding computation power and can be improvered.

