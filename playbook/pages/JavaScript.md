# JS

## Vanilla JS

__for loop__

`for (init; condition; final) { }`

`for (var i = 0; i < 3; i++) { }`

__conditionals__

```javascript
if (x.length === 0) {
  // do something
  } else if (x.length > 5) {
  // do something 
  } else {
  // if all else fails, do this
  }
```

__slice()__

takes in two args; start and stop. It will delete any items in an array that matches those locations.

```js
let arr = [1,2,3,4]

arr.splice(0,1)

console.log(arr)
>> 2,3,4
```

## Frameworks

- [Angular](Angular)

## Google Apps JS

### Sheets

#### onOpen Today()

In google sheets, open the sheet to the column with today's date.

- In `A1` add `=match(TODAY();A2:A;0)+1` to return the row number containing today's date.
- In the script editor create a new function with the following code:
  
```javascript
function onOpen() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var s = ss.getSheetByName("SheetX"); // change to sheet that has dates
  var r = s.getRange("A1").getValue(); // change A1 to the cell containing =match
  s.setActiveSelection(s.getRange("A" + r));
  }
```

##  Fullyear current year for footer

`<script>document.write(new Date().getFullYear())<script>`
