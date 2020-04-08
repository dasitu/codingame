package main

import (
	"fmt"
	"math"
	"math/rand"
	"os"
	"sort"
	"time"
)

func debug(a ...interface{}) {
	fmt.Fprintln(os.Stderr, a)
}

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

type chromosome string

type individual struct {
	chrom chromosome
	score float64
}

type population []individual

func (a population) Len() int {
	return len(a)
}

func (a population) Less(i, j int) bool {
	return a[i].score < a[j].score
}

func (a population) Swap(i, j int) {
	a[i], a[j] = a[j], a[i]
}

func createChromosome(n int) chromosome {
	b := make([]byte, n)
	for i := range b {
		b[i] = byte(rand.Intn(zoneCount))
	}
	return chromosome(string(b))
}

func createPopulation(popSize, chromSize int) population {
	p := make([]individual, popSize)
	for i := range p {
		c := createChromosome(chromSize)
		p[i] = individual{c, getScore(c)}
	}
	return p
}

func getScore(c chromosome) float64 {
	score := 0.0
	for id, z := range c {
		dPos := drones[myID][id].pos
		zPos := zones[z].pos
		round := int(getDistance(zPos, dPos) / 100)

	}
	return 0.0
}

func getMeanScore(p population) float64 {
	total := 0.0
	for _, i := range p {
		total += i.score
	}
	return total / float64(len(p))
}

func selection(p population) population {
	greadedRetainPercent := 0.3    // percentage of retained best fitting individuals
	NonGreadedRetainPercent := 0.2 // percentage of retained remaining individuals (randomly selected)
	totalCount := len(p)
	bestCount := int(float64(totalCount) * greadedRetainPercent)
	randCount := int(float64(totalCount) * NonGreadedRetainPercent)
	selected := make([]individual, 0)
	sort.Sort(sort.Reverse(p))
	selected = append(selected, p[:bestCount]...)
	for i := 0; i < randCount; i++ {
		min := bestCount
		max := totalCount - 1
		randIndex := rand.Intn(max-min+1) + min
		selected = append(selected, p[randIndex])
	}
	return population(selected)
}

func crossover(c1, c2 chromosome) chromosome {
	l := len(c1) / 2
	return c1[:l] + c2[l:]
}

func mutation(c chromosome) chromosome {
	newLetter := rand.Intn(zoneCount)
	randIndex := rand.Intn(len(c))
	return c[:randIndex] + chromosome(string(newLetter)) + c[randIndex+1:]
}

func generation(p population) population {
	var newGeneration population
	selected := selection(p)
	newGeneration = append(newGeneration, selected...)
	for len(newGeneration) < len(p) {
		twoRandInt := rand.Perm(len(selected))
		p1 := selected[twoRandInt[0]]
		p2 := selected[twoRandInt[1]]
		c := mutation(crossover(p1.chrom, p2.chrom))
		child := individual{c, getScore(c)}
		newGeneration = append(newGeneration, child)
	}
	return newGeneration
}

// global variable can be used by all functions
var playerCount, myID, dronesCount, zoneCount int
var zones []zone

// all drones [playerID][DroneID]
var drones [][]drone
var zeroPos coord = coord{0, 0}

func main1() {
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
	debug("avg count:", avgDCount)

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
		debug("my drones:", drones[myID])
		debug("all drones:", drones)

		// GA started
		rand.Seed(time.Now().UnixNano())
		chromSize := dronesCount
		popSize := 10
		p := createPopulation(popSize, chromSize)
		lastScore := 0.0
		answer := chromosome("")
		for answer == "" {
			p = generation(p)
			debug("mean score:", getMeanScore(p))
			for _, i := range p {
				if i.score == lastScore {
					answer = i.chrom
				}
			}
		}
		debug("avg count:", avgDCount)
		for i := 0; i < dronesCount; i++ {
			fmt.Println(zones[int(answer[i])].pos)
		}
	}
}
