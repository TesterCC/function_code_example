package main

import (
	"fmt"
	"os"
)

// 在Go语言中，使用os.Stat()函数并检查返回错误来判断文件是否存在

func main() {
	file := "./a.txt"
	// _, err := os.Stat(file)  // if don't print file size, comment it
	fileInfo, err := os.Stat(file)

	if os.IsNotExist(err) {
		// 如果os.IsNotExist(err)为true，说明文件不存在
		fmt.Println("File doesn't exist.")
	} else {
		fmt.Println("File exist.")
		fmt.Println("File size: ", fileInfo.Size(), "bytes")
	}
}
