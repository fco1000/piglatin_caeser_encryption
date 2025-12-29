package main

import (
	"fmt"
	cc "pig_caeser/caeser_cypher"
	pg "pig_caeser/pig_latin"
)

func main() {
	fmt.Print("Test value: ")
	testValue := "Hello world! and, welcome a shout of greetings"
	fmt.Println(testValue)

	fmt.Print("pig latin converted: ")
	pigTest := pg.PigLatinConv(testValue)
	fmt.Println(pigTest)

	fmt.Print("pig latin unconverted: ")
	pigTest2 := pg.PigLatinDeconv(pigTest)
	fmt.Println(pigTest2)

	fmt.Print("caeser cypher converted: ")
	caeserTest1 := cc.CaeserCypher(pigTest, 14)
	fmt.Println(caeserTest1)

	fmt.Print("caeser cypher unconverted: ")
	caeserTest2 := cc.CaeserDecypher(caeserTest1, 14)
	fmt.Println(caeserTest2)
}
