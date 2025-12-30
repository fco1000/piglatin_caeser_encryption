package pig_caesar

func CaeserCypher(input string, key int) string {
	if input == "" {
		return "enter valid input"
	} else if key < 1 || key > 25 {
		return "enter valid key value above 1 but below 25"
	}

	result := ""
	var ch rune

	for _, char := range input {
		if char >= 'a' && char <= 'z' { // lowercase
			ch = ('a' + (char-'a'+rune(key))%26)
			result += string(ch)
		} else if char >= 'A' && char <= 'Z' { // uppercase
			ch = ('A' + (char-'A'+rune(key))%26)
			result += string(ch)
		} else { // all other characters
			result += string(char)
		}

	}
	return result
}

func CaeserDecypher(input string, key int) string {
	if input == "" {
		return "Enter valid input value"
	}
	if key < 1 || key > 25 {
		return "Enter valid key value"
	}

	result := ""
	var ch rune

	for _, char := range input {
		if char >= 'a' && char <= 'z' {
			ch = ('a' + (char-'a'-rune(key)+26)%26) // adding 26 to avoid negative values
			result += string(ch)
		} else if char >= 'A' && char <= 'Z' {
			ch = ('A' + (char-'A'-rune(key)+26)%26)
			result += string(ch)
		} else {
			result += string(char)
		}
	}
	return result
}
