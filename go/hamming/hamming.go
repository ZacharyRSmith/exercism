/*
Package hamming calculates the Hamming difference between two DNA strands.
*/
package hamming

import "errors"

const testVersion = 5

/*
Distances calculates the Hamming difference between two DNA strands.
*/
func Distance(a, b string) (int, error) {
  dist := 0

  if len(a) != len(b) {
    return -1, errors.New("Strands must be of the same length.")
  }
  for i := 0; i < len(a); i++ {
    if a[i] != b[i] {
      dist += 1
    }
  }

  return dist, nil
}
