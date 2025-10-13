package main

import "fmt"

var version string	// a variable for setting version information through ldflag in build

func main() {
	fmt.Print("Example %s\n", version)
}