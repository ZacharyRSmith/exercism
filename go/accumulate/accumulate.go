/*
Package accumulate exports the Accumulate func.
*/
package accumulate

const testVersion = 1

/*
Accumulate,
WHEN given a collection and an
operation to perform on each element of the collection,
THEN returns a new
collection containing the result of applying that operation to each element of
the input collection.
*/
func Accumulate(input []string, fn func(string) string) []string {
	output := make([]string, len(input))

	for i, item := range input {
		output[i] = fn(item)
	}

	return output
}
