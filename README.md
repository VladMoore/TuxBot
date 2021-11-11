# <b>TuxBot</b>
## Introduction
This is my first ever bot! And I'd like to make it free so anyone can use, contribute, and learn from it, this bot is a major learning experience for me, and I hope it can help others out!

## Usage
*arguements surrounded by `[]`'s are required fields, `()` are optional fields*
* rand `[length]` `[dType]` `(blockSize)`
  * `length`: Amount of numbers to generate.
  * `dType`: The data type must be ‘uint8’ (returns integers between 0–255), ‘uint16’ (returns integers between 0–65535) or hex16.
  * `blockSize`: refers to the amount of blocks, only required in Hex16, disregard if using Uint.
  * Description: This command functions similar to how the RanInt# function works on a standard scientific calculator. However this uses quantum computing to generate 'true' random integers (Check ANU QRNG attached resource).
* ip `[IP Address]`
  * `IP Address`: IP Address you wish to lookup. 
  *  Description: Provides IP Address information in a nice embed format.
* ping
  * Description: returns the bot's latency in miliseconds rounded.

##  RoadMap
* Created the `rand` command along with the `ping` command ~ 6/11/2021 (DD/MM/YYYY).
* Created the `ip` command ~ 10/11/2021 (DD/MM/YYYY)

##  Resources
 * Random numbers are based on the [ANU QRNG](https://qrng.anu.edu.au/contact/api-documentation/) API.
