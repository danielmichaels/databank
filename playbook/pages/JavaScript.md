# JS

## Vanilla JS

## <Insert Framework>

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
