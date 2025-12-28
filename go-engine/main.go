package main

import (
	"fmt"
	pg "pig_caeser/pig_latin"
)

func main() {
	pigTest := pg.PigLatinConv("Hello world! and, welcome a shout of greetings")
	fmt.Println(pigTest)
	pigTest2 := pg.PigLatinDeconv(pigTest)
	fmt.Println(pigTest2)
}
