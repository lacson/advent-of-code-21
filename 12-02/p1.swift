#!/usr/bin/swift

import Foundation

class DirectionParser {
    var depth: Int
    var horizontal: Int

    func process(line: String) {
        let splitLine = line.split(separator: " ")
        if (splitLine[0] == "forward") { self.horizontal += Int(splitLine[1])! }
        else if (splitLine[0] == "up") { self.depth -= Int(splitLine[1])! }
        else if (splitLine[0] == "down") { self.depth += Int(splitLine[1])! }
        else { print("Unrecognized option \(splitLine[0])") }
    }

    init(filePath: String) {
        self.depth = 0
        self.horizontal = 0
        // this should be chunked, but chunking reading
        // looks stupid af
        do {
            let fileURL = URL(fileURLWithPath: filePath)
            let data = try String(contentsOf: fileURL)
            let lines = data.split(whereSeparator: \.isNewline)
            for line in lines {
                self.process(line: String(line))
            }
        }
        catch { print("Something bad happened") }
    }
}

let d = DirectionParser(filePath: CommandLine.arguments[1])
print(d.horizontal * d.depth)
