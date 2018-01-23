/*
Package acronym handles converting a phrase to its acronym.
*/
package acronym

import "fmt"
import "strings"

const testVersion = 3

/*
Abbreviate converts a phrase to its acronym.
*/
func Abbreviate(input string) string {
  res := ""

  fields := strings.Fields(input)
  for _, field := range fields {
    fmt.Println(field)
    res += strings.ToUpper(string(field[0]))
  }

  return res
}
