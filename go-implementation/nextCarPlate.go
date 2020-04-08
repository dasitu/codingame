// https://www.codingame.com/ide/puzzle/next-car-license-plate

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
	// scanner := bufio.NewScanner(os.Stdin)
	// scanner.Buffer(make([]byte, 1), 1)

	// scanner.Scan()
	// x := scanner.Text()

	// var n int
	// scanner.Scan()
	// fmt.Sscan(scanner.Text(), &n)

	x := "ER-963-DF"
	n := 87654321

	res := strings.SplitN(x, "-", -1)
	fmt.Fprintln(os.Stderr, n)
	fmt.Fprintln(os.Stderr, res)
	str := make([]int, 5)
	var err error
	str[0], err = strconv.Atoi(res[1])
	if err == nil {
		str[1] = int(res[2][1])
		str[2] = int(res[2][0])
		str[3] = int(res[0][1])
		str[4] = int(res[0][0])
	}

	increasedValues := make([]int, 5)
	posIndex := 0
	digitLeft := n / 999
	increasedValues[posIndex] = n % 999

	for posIndex < 4 {
		posIndex++
		increasedValues[posIndex] = digitLeft % 26
		digitLeft = digitLeft / 26
	}

	var output string
	for i := range str {
		newValue := str[i] + increasedValues[i]
		// A==65, Z==90
		start := 64
		upper := 90
		if i == 0 {
			start = 0
			upper = 999
		}

		if newValue > upper {
			newValue = (newValue - upper) + start
			increasedValues[i+1]++
		}
		str[i] = newValue
		if i == 0 {
			output += fmt.Sprintf("%03d", newValue)
		} else {
			output += string(newValue)
		}
	}
	fmt.Fprintln(os.Stderr, output)
	fmt.Println(string(output[6]) + string(output[5]) + "-" + string(output[0:3]) + "-" + string(output[4]) + string(output[3]))
}
