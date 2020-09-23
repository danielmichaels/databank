package main

import (
	"encoding/xml"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)
/*
its verbose but Go makes JSON and XML easy long term
As there is no need for converting things to objects or
arcane ['xzy'] like in Python.
 */
type Rss struct {
	XMLName xml.Name `xml:"rss"`
	Version string   `xml:"version,attr"`
	Channel Channel  `xml:"channel"`
}

type Channel struct {
	XMLName       xml.Name `xml:"channel"`
	Ttl           int      `xml:"ttl"`
	Link          string   `xml:"link"`
	Description   string   `xml:"description"`
	Language      string   `xml:"language"`
	Copyright     string   `xml:"copyright"`
	LastBuildDate string   `xml:"lastBuildDate"`
	Image         Image    `xml:"image"`
	Item          []Item   `xml:"item"`
}

type Image struct {
	XMLName xml.Name `xml:"image"`
	Url     string   `xml:"url"`
	Title   string   `xml:"title"`
	Link    string   `xml:"link"`
}

type Item struct {
	XMLName      xml.Name `xml:"item"`
	Title        string   `xml:"title"`
	Description  string   `xml:"description"`
	Brand        string   `xml:"brand"`
	Date         string   `xml:"date"`
	Price        float32  `xml:"price"`
	TradingName  string   `xml:"trading-name"`
	Address      string   `xml:"address"`
	Phone        string   `xml:"phone"`
	Latitude     string   `xml:"latitude"`
	Longitude    string   `xml:"longitude"`
	SiteFeatures string   `xml:"site-features"`
}

func getXml(url string) ([]byte, error) {
	// Always with the err, such Go
	resp, err := http.Get(url)
	if err != nil {
		return []byte{}, fmt.Errorf("GET Error: %v", err)
	}
	// defer so we can parse it
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return []byte{}, fmt.Errorf("Status Error: %v", resp.StatusCode)
	}

	// reads in the body content
	data, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return []byte{}, fmt.Errorf("Read Body: %v", err)
	}

	return data, nil
}

func main() {
	// we will be returned bytes which then need to be converted into human readable information
	xmlBytes, err := getXml("http://fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS")
	if err != nil {
		log.Printf("Failed to get XML: %v", err)
	}
	// instantiate the Rss struct
	rss := Rss{}
	// unmarshal is where the bytes are turned into text
	_ = xml.Unmarshal(xmlBytes, &rss)
	fmt.Println("Rss Version: " + rss.Version)
	for _, item := range rss.Channel.Item {
		fmt.Println(item.Description, item.Price)
	}
}

