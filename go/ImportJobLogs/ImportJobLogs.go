/*9-01-18@nikhil
This will use PaperCut WebXML API to to connect PaperCut.
This will  read the CSV and import Job logs from "c:\temp\Joblog_template.csv" to PaperCut Server
User Has to Drfine as their environment> AuthToken, AppServer, Port variable, defined afer comment containg string ##UserDefine

*/

package main

import (
	"bufio"
	"bytes"
	"encoding/csv"
	"encoding/xml"
	"fmt"
	//	"io/ioutil"
	//"log"
	"net/http"
	"os"
	"strings"
	"time"
)

// ##UserDefine Define all Auth_tokn , IP/host and port.
var AuthToken = "token"
var AppServer = "127.0.0.1"
var Port = "9191"
var ServerURL = "http://" + AppServer + ":" + Port + "/rpc/api/xmlrpc"

// Initiating web Cleint connection
var client = &http.Client{}

//Define the XML stracture and initialized V as struct.
type Param struct {
	Arg1 string `xml:"value>string"`
}
type JobProcess struct {
	XMLName xml.Name `xml:"methodCall"`
	Method  string   `xml:"methodName"`
	Param   [2]Param `xml:"params>param"`
}

var V JobProcess

func importJob(jobString string) {
	//Add the job String to V Struct
	V.Param[1].Arg1 = jobString
	//Marshell body of message
	output, err := xml.MarshalIndent(V, "  ", "    ")
	if err != nil {
		fmt.Printf("error: %v\n", err)
	}
	// Intitiate the http request format.
	req, err := http.NewRequest("POST", ServerURL, bytes.NewBuffer([]byte(output)))
	req.Header.Add("Content-Type", "text/xml")
	// Execute the http request.
	resp, err := client.Do(req)
	//, err := ioutil.ReadAll(resp.Body)
	resp.Body.Close()
	//	if err != nil {
	//	log.Fatal(err)
	//}
	//println("What I got")
	//log.Println(string(data))
}

func main() {
	// Device JOb type and Auth_token
	V.Method = "api.processJob"
	V.Param[0].Arg1 = AuthToken

	//CSV parse that contain jobs
	f, _ := os.Open("C:\\pc\\go\\JobLogImport\\printlog_template.csv")
	r := csv.NewReader(bufio.NewReader(f))
	record, _ := r.ReadAll()
	// Reader the header of CSV file
	header := record[0]
	//fmt.Println(header)
	var jobString, dt1, d string
	var dt []string
	var t time.Time
	//define the time format of imput to read
	format := "3:04:05 PM"

	// Processing input rows
	fmt.Print("Processing Row: ")
	for i, row := range record[1:] {
		fmt.Print(i+1, " ")
		// get first three manodotery feild from header and row
		jobString = header[0] + "=" + row[0] + "," + header[1] + "=" + row[1] + "," + header[2] + "=" + row[2]
		// Correct the Time Format as per jobprcess time syntex
		if row[3] != "" {
			//split the date and time based on tab between them
			dt = strings.Split(row[3], "\t")
			// Replace - with nothing
			d = strings.Replace(dt[0], "-", "", 2)
			// Parse the time based on predefine format
			t, _ = time.Parse(format, dt[1])
			// concatinating date and time in  ISO8601 simple date-time: yyyyMMddTHHmmss  format
			dt1 = d + "T" + t.Format("150404")
			//Added time to job string
			jobString = jobString + "," + header[3] + "=" + dt1
		}
		// adding rest of elent to to jobstring
		j := 4
		for _, element := range row[4:] {
			if element != "" {
				jobString = jobString + "," + header[j] + "=" + row[j]
			}
			j = j + 1
		}
		importJob(jobString)

	}

}
