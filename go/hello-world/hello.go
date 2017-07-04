/*
Package hello exports HelloWorld.
*/

// +build !example
package hello

const TestVersion = 1

/*
HelloWorld returns a greeting.
*/
func HelloWorld(name string) string {
	if name == "" {
		name = "World"
	}
	return "Hello, " + name + "!"
}
