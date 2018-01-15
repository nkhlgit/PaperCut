/*9-01-18@nikhil
This is to Import all jobs from C:\Tmp directory from JobLogs_Template.csv
*/

package main

import (
	"bufio"
	"bytes"
	"encoding/csv"
	"encoding/xml"
	"fmt"
	"net/http"
	"os"
	"strings"
	"time"
)

func main() {
	//CSV parse that contain jobs
	f, _ := os.Open("C:\\tmp\\JobLogs_Template.csv")
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

	// Initiating web Cleint connection
	client := &http.Client{}

	//Define the XML stracture
	type Param struct {
		Arg1 string `xml:"value>string"`
	}
	type JobProcess struct {
		XMLName xml.Name `xml:"methodCall"`
		Method  string   `xml:"methodName"`
		Param   [2]Param `xml:"params>param"`
	}
	// Assiging value to XML Variable
	v := &JobProcess{Method: "api.processJob"}
	v.Param[0].Arg1 = "token"

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
		//fmt.Println(jobString)
		// jobStream assigned 2nd string for jobprocess
		v.Param[1].Arg1 = jobString
		//Marshell body of message
		output, err := xml.MarshalIndent(v, "  ", "    ")
		if err != nil {
			fmt.Printf("error: %v\n", err)
		}
		// Intitiate the http request format.
		req, err := http.NewRequest("POST", "http://127.0.0.1:9191/rpc/api/xmlrpc", bytes.NewBuffer([]byte(output)))
		req.Header.Add("Content-Type", "text/xml")
		// Execute the http request.
		client.Do(req)
		/*		resp, err :=
				data, err := ioutil.ReadAll(resp.Body)
						resp.Body.Close()
						if err != nil {
							log.Fatal(err)
						}
						//println("Whayt I got")
						//log.Println(string(data))
		*/
	}

}
