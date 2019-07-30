// single line comment
/* Multi-
line comment */

// A package clause starts every source file.
// Main is a special name declaring an executable rather than a library.
package main

// import declaration declares library packages referenced in this file.
import (
	"fmt"       // A package from Go's std lib
	"io/ioutil" // Implements some I/O functions
	m "math"    // Math library with alias 'm'
	"net/http"  // Web server stuff
	"os"        // Allows working with local file system
	"strconv"
)

// A function definition. Main is special. It is the entry point for
// the executable program.
func main() {
	// Println outputs a line to stdout.
	// it comes from "fmt"
	fmt.Println("Hellow World")

	// call another function within this package
	beyondHello()
	// Go uses camelCase, unfortunately.
}

// Functions have parameters in parentheses.
// If there are no parameters, empty parentheses are still a requirement.
func beyondHello() {
	var x int // Variable declaration. Var's must be declared before use.
	x = 3     // Var assignment.
	// "Short" declarations use := to infer type, declare, and assign.
	y := 4
	sum, prod := learnMultiple(x, y)        // function returns two values
	fmt.Println("sum:", sum, "prod:", prod) // simple output
	learnTypes()
}

/* multiline comment here
Functions can have parameters and (multiple) return values
Here 'x', 'y' are the arguments and 'sum', 'prod' is the signature (what's returned)
Note that 'x' and 'sum' receive the type 'int'
*/
func learnMultiple(x, y int) (sum, prod int) {
	return x + y, x * y // return two values
}

// Some built-in types and literals.
func learnTypes() {
	// Short declaration usually gives you what you want.
	str := "Learn Go!" // string type

	s2 := `A "raw" string literal 
	can include line breaks.` // same string type
	// non-ASCII literal
	g := 'Σ'     // rune type, alias for int31, holds unicode
	f := 3.14159 // float64, an IEEE-754 64-bit floating point number.
	c := 3 + 4i  // complex128, represented internally with two float64's.

	// var syntax with initializers
	var u uint = 7 // Unsigned, but implementation dependent size as with int
	var pi float32 = 22. / 7

	// Conversion syntax with a short declaration.
	n := byte('\n') // byte is an alias for uint8

	var a4 [4]int // Arrays have a size fixed at compile time.
	// An array of 4 ints, initalised to all 0
	a5 := [...]int{3, 1, 5, 10, 100} // An array of init with fixed size of five
	// elements; 3,1,5,10,100

	// Slices have dynamic size. Arrays and slices each have advantages
	// but use cases for slices are much more common.
	s3 := []int{4, 5, 9}    // Compared to a5, not ellipsis here.
	s4 := make([]int, 4)    // allocates slice of 4 ints, init to all 0.
	var d2 [][]float64      // Decalaration only, nothing allocated here.
	bs := []byte("a slice") // type conversion syntax.

	// Because they are dynamic slices can be appended on demand.
	// To append elements to a slice, the built-in append() func is used.
	// First argument is a slice to which we are appending. Commonly,
	// the array variable is updated in place, as in example below.
	s := []int{1, 2, 3}    // Result is a slice of length 3.
	s = append(s, 4, 5, 6) // added 3 elements. Slice now length of 6.
	fmt.Println(s)         // Updated slice is now [1 2 3 4 5 6]

	// To append another slice, instead of list of atomic elements we can
	// pass a reference to a slice or slice literal like this, with a
	// trialling ellipsis, meaning take a slice and unpack its elements,
	// appending them to slice s.
	s = append(s, []int{7, 8, 9}...)
	fmt.Println(s)        // now is [1 2 3 4 5 6 7 8 9]
	p, q := learnMemory() // Decalres p,q to be type pointer to int.
	fmt.Println(*p, *q)   // * follows a pointer. This prints two ints.

	// Maps are dynamically growable associative array type, like a hash or dict in other languages.
	m := map[string]int{"three": 3, "four": 4}
	m["one"] = 1

	// Unused variables are a error in Go.
	// Underscores discard the value and appear "used" to the compiler.
	_, _, _, _, _, _, _, _, _, _ = str, s2, g, f, u, pi, n, a5, s4, bs
	// Ussually you use it to ignore one of the return values of a func
	// for example, in a script you might ignore error values returned from os.Create, except for the file we created.
	file, _ := os.Create("output.txt")
	fmt.Fprint(file, "This is how we write a file in Go!")
	file.Close()

	// Output of course counts as using a variable
	fmt.Println(s, c, a4, s3, d2, m)

	learnFlowControl() // flow control, yo!
}

// In go we can have functions that return named values
// Assigning a name to the type being returned in the function decalration line
// allows us to easuly return multiple points in a function as well as to
// only use the return keyword, without anything further (naked return)
func learnNamedReturns(x, y int) (z int) {
	z = x * y
	return // z is implicitly returned
}

// Go is garbage collected. It has pointers but no pointer arthmetic
// You can make mistakes with nil pointers by not incrementing them
func learnMemory() (p, q *int) {
	// Named return balies p and q have type point to int
	p = new(int) // built in func new allocates memory
	// The allocated int is init to 0, p is no longer Null
	s := make([]int, 20) // allocate 20 ints to single block of memory
	s[3] = 7             // Assign one of them
	r := -2              // Declare another local var
	return &s[3], &r     // & takes the address of an object
}

func expensiveComputation() float64 {
	return m.Exp(10)
}

func learnFlowControl() {
	// If statements require curly brackets, and do not require parenthesis
	if true {
		fmt.Println("told ya!")
	}
	// formatting is standardized by "go fmt"
	if false {
		// pout
	} else {
		// gloat
	}

	// use switch in preference to chained if statements
	x := 42.0
	switch x {
	case 0:
	case 1:
	case 42:
		// cases do not fall thru
		/*
			There is a `fallthrough` heyword though
		*/
	case 43:
		// never reaches this
	default:
		// optional
	}
	// Like if, for doesn't use parens either.
	// Var's declared in for and if are local in scope.
	for x := 0; x < 3; x++ { // ++ is a statement
		fmt.Println("iteration", x)
	}

	// For is the only loop, but we can still do while.
	for { // while/ infinite loop
		break    // kills while
		continue // doesn't reach me
	}

	// You can use range to iterate over an array, a slice, a string, a map, a channel.
	// range returns one channel or two values.
	for key, value := range map[string]int{"one": 1, "two": 2, "three": 3} {
		fmt.Printf("key=%s, value=%d\n", key, value)
	}
	// if you only need the value, use underscores
	for _, name := range []string{"bob", "bill", "joe"} {
		fmt.Printf("hello, %s\n", name)
	}

	// as with for, := in an if statement means to declare and assign
	// y first, then test y > x.
	if y := expensiveComputation(); y > x {
		x = y
	}

	// Function literals are closures.
	xBig := func() bool {
		return x > 10000 // Referneces x declared above switch statement.
	}
	x = 99999
	fmt.Println("xBig:", xBig()) // true
	x = 1.3e3                    // this makes x == 1300
	fmt.Println("xBig:", xBig()) // now false

	// whats more is function literals may be defined and called inline,
	// acting as an argument to function, as long as:
	// a) fun literal is called immediately (),
	// b) result type matches expected type of argument.
	fmt.Println("Add + double two numbers: ",
		func(a, b int) int {
			return (a + b) * 2
		}(10, 2)) // called with args 10 and 2
	// => add + double two nums: 24

	// when you need it, you'll love it.
	goto love
love:

	learnFunctionFactory() // func returning func is fun(3)(3)
	learnDefer()      // important keyword
	learnInterfaces() // Good stuff here
}

func learnFunctionFactory() {
	// next two are equivilent but with the next being more practical
	fmt.Println(sentanceFactory("summer")("a beautiful", "day!"))

	d := sentanceFactory("summer")
	fmt.Println(d("A beautiful", "day!"))
	fmt.Println(d("A lazy", "afternoon!"))
}

// Decorateors are commin in other languages. Same can be done in Go
// with function literals that accept arguments.
func sentanceFactory(mystring string) func(before, after string) string {
	return func(before, after string) string {
		return fmt.Sprintf("%s %s %s", before, mystring, after)
	}
}

func learnDefer() (ok bool) {
	// Deferred statements are executed just be the function returns.
	defer fmt.Println("deferred statements are executed in reverse (LIFO) order.")
	defer fmt.Println("\n This line printed first because..")
	// Defer is commonly used to close a file, so the func closing file is close to func that opens file.
	return true
}

// define Stringer as an interface type with one method, String
type Stringer interface {
	String() string
}

// define pair as struct with two fields, ints named x and y
type pair struct {
	x, y int
}

// define a method on type pair. Pair now implements Stringer because Pair has defined all the methods in the interface.
func (p pair) String() string { // p is called the "reciever"
	// Sprintf is another public function in "fmt"
	// Dot syntax references fields of p.
	return fmt.Sprintf("(%d, %d)", p.x, p.y)
}

func learnInterfaces() {
	// Brace suntax is a "struct literal", It evals to an init
	// struct. The := syntax declares and initalised p to the this struct.
	p := pair{3, 4}
	fmt.Println(p.String()) // call string method of p, of type pair.
	var i Stringer          // declare i of interface type Stringer
	i = p                   // Valid becuse pair implements Stringer
	// Call String method of i, of type Stringer. Output same as above.
	fmt.Println(i.String())

	// Func's in the fmt package call the String method to ask an object
	// for a printable representation of itself.
	fmt.Println(p) // OUtput same as above
	fmt.Println(i) // same as above.

	learnVariadicParams("great", "Learning", "here!")
}

// functions can have variadic parameters.
func learnVariadicParams(myStrings ...interface{}) {
	// iterate each value of the variadic.
	// The underbar here is ignoring the index argument of the array.
	for _, param := range myStrings {
		fmt.Println("param:", param)
	}
	// pass variadic value as a variadic parameter.
	fmt.Println("params:", fmt.Sprintln(myStrings...))

	learnErrorHandling()
}

func learnErrorHandling() {
	// ", ok" idiom used to tell if something worked or not.
	m := map[int]string{3: "three", 4: "four"}
	if x, ok := m[1]; !ok { //ok will be false because 1 is not in the map.
		fmt.Println("no one there")
	} else {
		fmt.Print(x) // x would be the value, if it were in the map.
	}
	// An error value communicates not just "ok" but more about the problem.
	if _, err := strconv.Atoi("non-int"); err != nil { // _ discards value
		// prints `strconv.ParseInt: parsing "non-int": invalid syntax`
		fmt.Println(err)
	}
	// we'll revisit interfaces a little later. meanwhile,
	learnConcurrency()
}

// c is a channel, a concurrency-safe communication object.
func inc(i int, c chan int) {
	c <- i + 1 // <- is the "send" operator when a channel appears on the left
}

// we'll use inc to increment some numbers concurrently.
func learnConcurrency() {
	// smae make function used earlier to make a slice. Make allocates and
	// initiialises slices, maps, and channels.
	c := make(chan int)
	// start three concurrent goroutines. NUmbers bill be incremented
	// concurrently, perhaps in parallel if the machine is capable and
	// properly configured. All three send to the same channel.
	go inc(0, c) // go is a statement that starts a new goroutine.
	go inc(10, c)
	go inc(-805, c)
	// read three results from the channel and print them out.
	// there is no telling in what order the results will arrive!
	fmt.Println(<-c, <-c, <-c) // channel on the right, <- is "receive" operator.

	cs := make(chan string)       // anoter channel, this one handles strings.
	ccs := make(chan chan string) // a channel of string channels.
	go func() { c <- 84 }()       // start new goroutine just to send a value.
	go func() { cs <- "wordy" }() // again, for cs this time.

	// Select has syntax like a switch statement but each case involves
	// a channel operation. It selects case at random out of the cases
	// that are ready to communicate.
	select {
	case i := <-c: // the value rx can be assigned to a variable,
		fmt.Printf("it's a %T", i)
	case <-cs: // or the value rx can be discarded
		fmt.Println("it's a string")
	case <-ccs: // empty channel, not ready for communication.
		fmt.Println("didn't happen.")
	}
	// At this point a value was taken form either c or cs. One of the two
	// go routines started above has completed, the other will remain blocked.

	learnWebProgramming() // Go does it. You want it too!
}

// A single function from the package http starts a web server.
func learnWebProgramming() {
	// First parameter of the ListenAndServe is TCP address to listen to.
	// Second parameter is an interface, specifically http.Handler
	go func() {
		err := http.ListenAndServe(":808", pair{})
		fmt.Println(err) // don't ignore errors
	}()

	requestServer()
}

// Make pair an http.Handler by implementing its only method, ServeHTTP.
func (p pair) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	// Serve data with a method of http.ResponseWriter.
	w.Write([]byte("Your learnt Go in Y minutes!"))
}

func requestServer() {
	resp, err := http.Get("http://localhost:8080")
	fmt.Println(err)
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	fmt.Printf("\nWebserver said: `%s`", string(body))
}
