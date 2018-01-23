/*
Package raindrops converts a number to a string, the contents of which depend on the number's factors.
*/
package raindrops

import "strconv"

const testVersion = 3

/*
Convert converts a number to a string, the contents of which depend on the number's factors.

- If the number has 3 as a factor, output 'Pling'.
- If the number has 5 as a factor, output 'Plang'.
- If the number has 7 as a factor, output 'Plong'.
- If the number does not have 3, 5, or 7 as a factor,
  just pass the number's digits straight through.

## Examples

- 28's factors are 1, 2, 4, **7**, 14, 28.
  - In raindrop-speak, this would be a simple "Plong".
- 30's factors are 1, 2, **3**, **5**, 6, 10, 15, 30.
  - In raindrop-speak, this would be a "PlingPlang".
- 34 has four factors: 1, 2, 17, and 34.
  - In raindrop-speak, this would be "34".
*/
func Convert(num int) string {
	res := ""

	if num%3 == 0 {
		res += "Pling"
	}
	if num%5 == 0 {
		res += "Plang"
	}
	if num%7 == 0 {
		res += "Plong"
	}

	if res == "" {
		return strconv.Itoa(num)
	}
	return res
}

// Don't forget the test program has a benchmark too.
// How fast does your Convert convert? A: 1112 ns/op
