package codingame

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
	id         int
	pos        coord
	owner      int
	enemyCount int
	myDids     []int
}

type drone struct {
	id     int
	pos    coord
	target coord
}

func getDistance(pos1, pos2 coord) int {
	return int(math.Sqrt(float64(((pos1.x - pos2.x) * (pos1.x - pos2.x)) + ((pos1.y - pos2.y) * (pos1.y - pos2.y)))))
}

// check if d is in circle which center is c and range is r
func isInCircle(c coord, r int, d coord) bool {
	return ((d.x-c.x)*(d.x-c.x) + (d.y-c.y)*(d.y-c.y)) < r*r
}

func contains(s []int, e int) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func assignAvgDrones(z zone, avgCount int, myFreeDrones []int) []int {
	avgDid := make([]int, 0)
	shorter := int(math.Min(float64(z.pos.x), float64(z.pos.y)))
	scanRange := 100
	for shorter+scanRange < 1800 {
		for _, did := range myFreeDrones {
			if isInCircle(z.pos, scanRange, drones[myID][did].pos) {
				avgDid = append(avgDid, did)
				avgCount--
			}
			if avgCount == 0 {
				break
			}
		}

		// remove allocated drones from myFreeDrones to avoid add agian after increase range
		for _, aid := range avgDid {
			for i, v := range myFreeDrones {
				if v == aid {
					removeByIndex(myFreeDrones, i)
					break
				}
			}
		}

		if avgCount == 0 {
			break
		} else {
			scanRange += 100
		}
	}
	return avgDid
}

func getNearestZone(d drone) coord {
	var choosePos coord
	zid := 0
	var shortest int = 4000
	for _, z := range zones {
		dis := getDistance(z.pos, d.pos)
		//fmt.Fprintf(os.Stderr, "%v->%v=%v\n", z.pos, z.pos, dis)
		if dis < shortest {
			shortest = dis
			choosePos = z.pos
			zid = z.id
		}
	}
	fmt.Fprintf(os.Stderr, "neraest zone for drone(%v) is %v \n", d.id, zid)
	return choosePos
}

func removeByIndex(s []int, i int) {
	s[i] = s[len(s)-1] // Copy last element to index i.
	s[len(s)-1] = 0    // Erase last element (write zero value).
	s = s[:len(s)-1]   // Truncate slice.
}

func updateZoneData() {
	searchRange := 100
	for zi, z := range zones {
		enemyCount := 0
		myids := make([]int, 0)
		for pid, drs := range drones {
			for did, d := range drs {
				if isInCircle(z.pos, searchRange, d.pos) {
					if pid == myID {
						myids = append(myids, did)
					} else {
						enemyCount++
					}
				}
			}
		}
		zones[zi].enemyCount = enemyCount
		zones[zi].myDids = myids
	}
}

func calculateFreeDrones(avgCount int) []int {
	freeids := make([]int, 0)
	for _, z := range zones {
		myCount := len(z.myDids)
		// myzone and mycount is bigger than enemy
		if z.enemyCount < myCount && z.owner == myID {
			freeCount := myCount - z.enemyCount - avgCount
			for i := 0; i < freeCount; i++ {
				freeids = append(freeids)
			}
		}
	}
	return freeids
}

// global variable can be used by all functions
var playerCount, myID, dronesCount, zoneCount int
var zones []zone

// all drones [playerID][DroneID]
var drones [][]drone
var zeroPos coord = coord{0, 0}

func main() {
	// read basic input
	fmt.Scan(&playerCount, &myID, &dronesCount, &zoneCount)
	zones = make([]zone, zoneCount)
	// read zone position input
	for i := 0; i < zoneCount; i++ {
		zones[i].id = i
		fmt.Scan(&zones[i].pos.x, &zones[i].pos.y)
	}
	// initial all drones space
	drones = make([][]drone, playerCount)
	for i := 0; i < playerCount; i++ {
		drones[i] = make([]drone, dronesCount)
	}
	// at least one drone is needed for each zone
	avgDCount := int(math.Max(1, float64(dronesCount/zoneCount)))
	fmt.Fprintln(os.Stderr, "avg count:", avgDCount)

	// game loop started forever
	for {
		// read owner input
		for i := 0; i < zoneCount; i++ {
			fmt.Scan(&zones[i].owner)
		}
		// read drone input
		for i := 0; i < playerCount; i++ {
			for j := 0; j < dronesCount; j++ {
				fmt.Scan(&drones[i][j].pos.x, &drones[i][j].pos.y)
				drones[i][j].id = j
			}
		}
		fmt.Fprintln(os.Stderr, "my drones:", drones[myID])
		fmt.Fprintln(os.Stderr, "all drones:", drones)

		updateZoneData()
		fmt.Fprintln(os.Stderr, "updated all zones:", zones)
		// assign avg count to every zone
		// create all my no target drone id slice to void duplicated allocation
		myFreeDroneIds := make([]int, dronesCount)
		for i := 0; i < dronesCount; i++ {
			// just assign these no target drone, as this is just starting strategy
			if drones[myID][i].target == zeroPos {
				myFreeDroneIds[i] = i
			}
		}
		// findout these free drones
		fids := calculateFreeDrones(avgDCount)
		for _, fid := range fids {
			if contains(myFreeDroneIds, fid) {
				continue
			}
			myFreeDroneIds = append(myFreeDroneIds, fid)
		}

		fmt.Fprintf(os.Stderr, "free drones:%v\n", myFreeDroneIds)
		// start to allocate these no target drones zone by zone
		for zi, z := range zones {
			dids := assignAvgDrones(z, avgDCount, myFreeDroneIds)
			fmt.Fprintf(os.Stderr, "dids for zone(%v):%v\n", zi, dids)
			// update the target of these drones to the center of the zone
			for _, d := range dids {
				drones[myID][d].target = z.pos
				// remove allocated drones for next use
				for i, v := range myFreeDroneIds {
					if v == d {
						removeByIndex(myFreeDroneIds, i)
						break
					}
				}
			}
		}
		fmt.Fprintln(os.Stderr, "my drones after allocate:", drones[myID])

		for i := 0; i < dronesCount; i++ {
			// drone already have target and not achived yet, keep moving
			if drones[myID][i].target != drones[myID][i].pos && drones[myID][i].target != zeroPos {
				fmt.Println(drones[myID][i].target)
				continue
			}
			// drone does not have any target, just goto nearest zone
			move := getNearestZone(drones[myID][i])
			drones[myID][i].target = move
			fmt.Println(move)
		}
	}
}
