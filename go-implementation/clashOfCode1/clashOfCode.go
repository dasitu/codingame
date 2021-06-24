package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, 1000000), 1000000)

	scanner.Scan()
	s := scanner.Text()
	_ = s // to avoid unused error

	words := strings.Fields(s)
	c := len(words)
	w := ""
	if c%2 != 0 {
		w = words[c/2]
	} else {
		i1 := c / 2
		i2 := i1 - 1
		w = words[i2] + words[i1]
	}

	fmt.Println(w)

}
