package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

const url string = "https://api.ipify.org/"

func ExtIP() (string, error) {
	resp, error := http.Get(url)

	if error != nil {
		return "", nil
	}
	ip, error := ioutil.ReadAll(resp.Body)

	if error != nil {
		return "", nil
	}
	return string(ip), nil

}

func main() {
	ip, _ := ExtIP()
	fmt.Printf("IP address: %v", ip)

}
