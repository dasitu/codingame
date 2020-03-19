package main

import (
	"fmt"
	"math"
	"os"
)

type coord struct {
	x int
	y int
}

func (c coord) String() string {
	return fmt.Sprintf("%v %v", c.x, c.y)
}

type zone struct {
	pos   coord
	owner int
}

type drone struct {
	pos    coord
	moving bool
	target coord
}

func getDistance(x1, y1, x2, y2 int) float64 {
	return math.Sqrt(float64((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)))
}

func getNearestZone(allZones []zone, myDrone drone, myID int) coord {
	var choosePos coord
	var shortest float64 = 4000
	for _, z := range allZones {
		if z.owner == myID {
			continue
		}
		dis := getDistance(z.pos.x, z.pos.y, myDrone.pos.x, myDrone.pos.y)
		fmt.Fprintf(os.Stderr, "%v->%v=%v\n", z.pos, z.pos, dis)
		if dis < shortest && dis != 0 {
			shortest = dis
			choosePos.x = z.pos.x
			choosePos.y = z.pos.y
		}
	}
	return choosePos
}

func main() {
	// playerCount: number of players in the game (2 to 4 players)
	// myID: ID of your player (0, 1, 2, or 3)
	// dronesCount: number of drones in each team (3 to 11)
	// zoneCount: number of zones on the map (4 to 8)
	var playerCount, myID, dronesCount, zoneCount int
	fmt.Scan(&playerCount, &myID, &dronesCount, &zoneCount)

	zones := make([]zone, zoneCount)
	// key is [playerID][DroneID], 01, 11
	drones := make([][]drone, playerCount)
	// initial all drones space
	for i := 0; i < playerCount; i++ {
		drones[i] = make([]drone, dronesCount)
	}

	for i := 0; i < zoneCount; i++ {
		// X: corresponds to the position of the center of a zone.
		// A zone is a circle with a radius of 100 units.
		var X, Y int
		fmt.Scan(&X, &Y)
		zones[i] = zone{coord{X, Y}, -1}
	}

	fmt.Fprintln(os.Stderr, "all zones:", zones)

	for {
		for i := 0; i < zoneCount; i++ {
			// TID: ID of the team controlling the zone (0, 1, 2, or 3) or -1 if it is not controlled.
			// The zones are given in the same order as in the initialization.
			fmt.Scan(&zones[i].owner)
		}
		for i := 0; i < playerCount; i++ {
			for j := 0; j < dronesCount; j++ {
				// DX: The first D lines contain the coordinates of drones of a player with the ID 0,
				// the following D lines those of the drones of player 1, and thus it continues until the last player.
				var pos coord
				fmt.Scan(&pos.x, &pos.y)
				drones[i][j].pos = pos
				if drones[i][j].target == pos {
					drones[i][j].moving = false
				}
			}
		}
		fmt.Fprintln(os.Stderr, "all drones:", drones)
		for i := 0; i < dronesCount; i++ {
			if drones[myID][i].moving == true {
				fmt.Println(drones[myID][i].target)
				continue
			}
			move := getNearestZone(zones, drones[myID][i], myID)
			drones[myID][i].target = move
			drones[myID][i].moving = true
			fmt.Println(move)
		}
	}
}
