# A) Preparation

To build `small_samples` on lcc3 one needs to first load the modules specified in `/ldcc3_helpers/modules.sh`.

>[!NOTE]
> Adding them to your `.bashrc` might make life easier for the future.

## delannoy
This program calculates the delannoy number for a given grid size n.
Furthermore, it checks the result with a predefined list and is therefore only
able to calculate a limited number of delannoy numbers.
The algorithm is recursive and therefore scales pretty drastically.
For an acceptable runtime that is not too short, to reduce the impact of random system noise I chose `n = 18`
