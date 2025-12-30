package pig_caesar

import "strings"

// import "fmt"

/*
there will be a text document that will have many words, sentenses and even paragraps
i need to have a way to isolate each word for conversion and then the converted word added to a new place where the pig latin text will be

take the whole thing,
then take the words, letters and symbols and group them as a word
once a space is reached, we stop and convert the word at hand and push it else where
we also ensure that the numbers and other symbols are maintained

the converted words should have their consonant clusters moved to the back of the word which will require some work
then the preferred suffix added to the end of the word
*/

func PigLatinConv(input string) string {
	if input == "" {
		return ""
	}
	result := ""
	words := []string{}
	words = strings.Split(input, " ")
	for i, word := range words {
		if isVowel(word[0]) {
			word = word + "-way"
		} else {
			word = moveFirstConsonantCluster(word) + "-ay"
		}
		if i < len(words)-1 {
			result = result + word + " "
		} else {
			result = result + word
		}
	}
	return result
}

func moveFirstConsonantCluster(word string) string {
	if word == " " {
		return word
	}
	i := 0
	for i < len(word) && !(isVowel(word[i])) {
		i++
	}
	if i == 0 || i == len(word) {
		return word
	}
	return word[i:] + "'" + word[:i] + "'" // adding apostrophes to mark the consonant cluster for later deconversion
}

func isVowel(b byte) bool {
	switch b {
	case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
		return true
	}
	return false
}

func PigLatinDeconv(input string) string {
	if input == "" {
		return ""
	}
	result := ""
	words := []string{}
	words = strings.Split(input, " ")
	for i, word := range words {
		if strings.Contains(word, "-way") {
			word = strings.TrimSuffix(word, "-way")
		} else if strings.Contains(word, "-ay") {
			word = strings.TrimSuffix(word, "-ay")
			word = ReplaceConsonantCluster(word)
		}

		if i < len(words)-1 {
			result = result + word + " "
		} else {
			result = result + word
		}
	}

	return result
}

func ReplaceConsonantCluster(word string) string {
	if word == "" {
		return word
	}
	first := strings.LastIndex(word, "'") // get the index of the last apostrophe
	if first == -1 {
		return word
	}
	rest := word[:first]                   // remove the apostrophe
	second := strings.LastIndex(rest, "'") // get the index for the second apostrophe
	if second == -1 {
		return word
	}
	cluster := word[second+1 : first] // get the consonant cluster using the indices of the apostrophes while excluding them
	base := word[:second]             // get the base word
	return cluster + base
}
