package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func calculateAverage(grades map[string]float64, numberOfSubjects int) float64 {
	var total float64
	for _, value := range grades {
		total += value
	}
	return total / float64(numberOfSubjects)
}

func main() {
	var grades = make(map[string]float64)
	var numberOfSubjects int
	var name string

	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter your name: ")
	name, _ = reader.ReadString('\n')
	name = strings.TrimSpace(name)

	fmt.Print("How many subjects did you take?: ")
	fmt.Scanln(&numberOfSubjects)

	for i := 0; i < numberOfSubjects; i++ {

		fmt.Print("Enter subject name: ")
		subject, _ := reader.ReadString('\n')
		subject = strings.TrimSpace(subject)

		var grade float64
		for {

			fmt.Printf("Enter grade for %s: ", subject)
			gradeInput, _ := reader.ReadString('\n')
			gradeInput = strings.TrimSpace(gradeInput)

			grade, _ = strconv.ParseFloat(gradeInput, 64)
			if grade >= 0 && grade <= 100 {
				break
			} else {
				fmt.Println("Invalid grade, please enter a valid grade between 0 and 100.")
			}
		}
		grades[subject] = grade
	}

	average := calculateAverage(grades, numberOfSubjects)

	fmt.Printf("Student's name: %s\n", name)
	for sub, val := range grades {
		fmt.Printf("%s: %.2f\n", sub, val)
	}
	fmt.Printf("Your average score is: %.2f\n", average)
}
